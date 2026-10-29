"use strict";

const STORAGE_KEY = "dsa-revision-progress-v1";
const THEME_KEY = "dsa-revision-theme-v1";
const DAY = 24 * 60 * 60 * 1000;

function getPreferredTheme() {
  try {
    const saved = localStorage.getItem(THEME_KEY);
    if (saved === "dark" || saved === "light") return saved;
  } catch {}
  return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  const themeMeta = document.querySelector('meta[name="theme-color"]');
  if (themeMeta) {
    themeMeta.setAttribute("content", theme === "dark" ? "#0b0f19" : "#f6f5ef");
  }
  const icon = document.querySelector("#theme-toggle-btn .theme-icon");
  const label = document.querySelector("#theme-label");
  if (icon && label) {
    if (theme === "dark") {
      icon.textContent = "☀️";
      label.textContent = "Light";
    } else {
      icon.textContent = "🌙";
      label.textContent = "Dark";
    }
  }
}

function toggleTheme() {
  const current = document.documentElement.getAttribute("data-theme") || getPreferredTheme();
  const next = current === "dark" ? "light" : "dark";
  try {
    localStorage.setItem(THEME_KEY, next);
  } catch {}
  applyTheme(next);
  displayMessage(`Switched to ${next} theme.`);
}

// Apply theme instantly on script parse to eliminate flash of light mode
applyTheme(getPreferredTheme());

const elements = {
  answer: document.querySelector("#answer"),
  answerGrid: document.querySelector("#answer-grid"),
  appMessage: document.querySelector("#app-message"),
  barLearning: document.querySelector("#bar-learning"),
  barMastered: document.querySelector("#bar-mastered"),
  breadcrumb: document.querySelector("#card-breadcrumb"),
  cardDifficulty: document.querySelector("#card-difficulty"),
  cardFreqPill: document.querySelector("#card-freq-pill"),
  cardLcPill: document.querySelector("#card-lc-pill"),
  cardLcText: document.querySelector("#card-lc-text"),
  cardNumber: document.querySelector("#card-number"),
  cardPattern: document.querySelector("#card-pattern"),
  cardPosition: document.querySelector("#card-position"),
  cardPrompt: document.querySelector("#card-prompt"),
  cardTitle: document.querySelector("#card-title"),
  cardTopic: document.querySelector("#card-topic"),
  codeBlock: document.querySelector(".code-block"),
  codeCaption: document.querySelector("#code-caption"),
  codeContainer: document.querySelector("#code-container"),
  codeRevealButton: document.querySelector("#code-reveal-button"),
  copyCodeButton: document.querySelector("#copy-code-button"),
  copyLabel: document.querySelector("#copy-label"),
  difficultyFilter: document.querySelector("#difficulty-filter"),
  dueCount: document.querySelector("#due-count"),
  emptyList: document.querySelector("#empty-list"),
  flashCard: document.querySelector("#flash-card"),
  groupFilter: document.querySelector("#group-filter"),
  hintBtnLabel: document.querySelector("#hint-btn-label"),
  hintCounter: document.querySelector("#hint-counter"),
  hintsBody: document.querySelector("#hints-body"),
  hintsDrawer: document.querySelector("#hints-drawer"),
  hintsStack: document.querySelector("#hints-stack"),
  hintToggleButton: document.querySelector("#hint-toggle-button"),
  languageSelect: document.querySelector("#language-select"),
  lcTopLink: document.querySelector("#lc-top-link"),
  masteredCount: document.querySelector("#mastered-count"),
  markdownModal: document.querySelector("#markdown-modal"),
  modalBody: document.querySelector("#modal-body"),
  modalCloseBtn: document.querySelector("#modal-close-btn"),
  modalRawLink: document.querySelector("#modal-raw-link"),
  modalTitle: document.querySelector("#modal-title"),
  nextButton: document.querySelector("#next-button"),
  nextHintButton: document.querySelector("#next-hint-button"),
  previousButton: document.querySelector("#previous-button"),
  problemCount: document.querySelector("#problem-count"),
  problemList: document.querySelector("#problem-list"),
  readmeModalBtn: document.querySelector("#readme-modal-btn"),
  readmeRawLink: document.querySelector("#readme-raw-link"),
  repoReadmeBtn: document.querySelector("#repo-readme-btn"),
  resultsLabel: document.querySelector("#results-label"),
  revealButton: document.querySelector("#reveal-button"),
  reviewState: document.querySelector("#review-state"),
  reviewedCount: document.querySelector("#reviewed-count"),
  searchInput: document.querySelector("#search-input"),
  shuffleButton: document.querySelector("#shuffle-button"),
  sourceCode: document.querySelector("#source-code"),
  statusFilter: document.querySelector("#status-filter"),
  themeToggleBtn: document.querySelector("#theme-toggle-btn"),
  topicFilter: document.querySelector("#topic-filter")
};

let cards = [];
let visibleCards = [];
let activeId = null;
let progress = {};
let codeRevealed = false;
let revealedHintCount = 0;
let rawLoadedCode = "";

/* --- HTML & Markdown Helpers --- */

function escapeHtml(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function formatInline(value) {
  let text = escapeHtml(value);
  text = text.replace(/`([^`]+)`/g, "<code>$1</code>");
  text = text.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  text = text.replace(/\*([^*]+)\*/g, "<em>$1</em>");
  return text;
}

function safeNoteHtml(markdown) {
  const blocks = String(markdown || "").trim().split(/\n\s*\n/).filter(Boolean);
  return blocks.map((block) => {
    const lines = block.split("\n").map((line) => line.trim()).filter(Boolean);
    if (lines.length && lines.every((line) => /^[-*+]\s+/.test(line))) {
      return `<ul>${lines.map((line) => `<li>${formatInline(line.replace(/^[-*+]\s+/, ""))}</li>`).join("")}</ul>`;
    }
    return `<p>${lines.map(formatInline).join("<br>")}</p>`;
  }).join("");
}

function renderMarkdownToHtml(md) {
  let text = String(md || "").replace(/\r\n/g, "\n");

  // Code blocks: ```lang ... ```
  text = text.replace(/```([a-zA-Z0-9_-]*)\n([\s\S]*?)```/g, (_, lang, code) => {
    const highlighted = highlightSyntax(code.trim(), lang || "java");
    return `<pre class="doc-code-block"><code>${highlighted}</code></pre>`;
  });

  // Table parser: | a | b |\n| --- | --- |\n| c | d |
  text = text.replace(/((?:^\|[^\n]+\|\n?)+)/gm, (match) => {
    const lines = match.trim().split("\n").filter(Boolean);
    if (lines.length < 2) return match;
    let html = '<div class="doc-table-wrap"><table class="doc-table">';
    let isHeader = true;
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      if (/^\|\s*[-:]+[-| :]*\|$/.test(line)) {
        isHeader = false;
        continue;
      }
      const cells = line.split("|").slice(1, -1).map((c) => c.trim());
      const tag = isHeader ? "th" : "td";
      html += `<tr>${cells.map((c) => `<${tag}>${formatInline(c)}</${tag}>`).join("")}</tr>`;
    }
    html += "</table></div>";
    return html;
  });

  // Headings
  text = text.replace(/^######\s+(.*)$/gm, "<h6>$1</h6>");
  text = text.replace(/^#####\s+(.*)$/gm, "<h5>$1</h5>");
  text = text.replace(/^####\s+(.*)$/gm, "<h4>$1</h4>");
  text = text.replace(/^###\s+(.*)$/gm, "<h3>$1</h3>");
  text = text.replace(/^##\s+(.*)$/gm, "<h2>$1</h2>");
  text = text.replace(/^#\s+(.*)$/gm, "<h1>$1</h1>");

  // Blockquotes
  text = text.replace(/^>\s+(.*)$/gm, '<blockquote class="doc-quote">$1</blockquote>');

  // Horizontal Rules
  text = text.replace(/^\s*[-*_]{3,}\s*$/gm, "<hr />");

  // Lists: - item or * item
  text = text.replace(/((?:^\s*[-*+]\s+[^\n]+\n?)+)/gm, (match) => {
    const items = match.trim().split("\n").map((line) => line.replace(/^\s*[-*+]\s+/, "").trim());
    return `<ul class="doc-list">${items.map((it) => `<li>${formatInline(it)}</li>`).join("")}</ul>`;
  });

  // Bold & Italic
  text = text.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  text = text.replace(/\*([^*]+)\*/g, "<em>$1</em>");

  // Inline Code
  text = text.replace(/`([^`]+)`/g, '<code class="doc-inline-code">$1</code>');

  // Markdown Links: [text](url)
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer" class="doc-link">$1 ↗</a>');

  // Paragraphs
  const blocks = text.split(/\n\s*\n/);
  return blocks
    .map((b) => {
      b = b.trim();
      if (!b) return "";
      if (/^<(?:h[1-6]|ul|ol|pre|table|div|blockquote|hr)/.test(b)) return b;
      return `<p class="doc-para">${b.replace(/\n/g, "<br />")}</p>`;
    })
    .join("\n");
}

/* --- Zero-Dependency Syntax Highlighter --- */

function highlightSyntax(code, language) {
  const lang = String(language || "java").toLowerCase();

  let tokenRegex;
  if (lang.includes("py")) {
    tokenRegex = /(#.*$)|("""[\s\S]*?"""|'''[\s\S]*?'''|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|\b(def|class|import|from|return|if|elif|else|for|while|in|is|not|and|or|lambda|with|as|try|except|finally|raise|yield|pass|break|continue|None|True|False|self)\b|\b(int|float|str|bool|list|dict|set|tuple|len|range|enumerate|zip|sum|min|max|abs|print)\b|\b(0x[0-9a-fA-F]+|\d+(?:\.\d+)?)\b|([a-zA-Z_$][a-zA-Z0-9_$]*)(?=\s*\()/gm;
  } else if (lang.includes("c") || lang.includes("cpp")) {
    tokenRegex = /(\/\/[^\n]*|\/\*[\s\S]*?\*\/)|("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|(^#\s*[a-zA-Z0-9_]+)|\b(auto|bool|break|case|catch|char|class|const|continue|default|delete|do|double|else|enum|explicit|extern|false|float|for|friend|goto|if|inline|int|long|mutable|namespace|new|nullptr|operator|private|protected|public|register|return|short|signed|sizeof|static|struct|switch|template|this|throw|true|try|typedef|typeid|typename|union|unsigned|using|virtual|void|volatile|while)\b|\b(string|vector|map|unordered_map|set|unordered_set|pair|queue|stack|deque|priority_queue|iostream|std)\b|\b(0x[0-9a-fA-F]+|\d+(?:\.\d+)?(?:[fFdDlL])?)\b|([a-zA-Z_$][a-zA-Z0-9_$]*)(?=\s*\()/gm;
  } else {
    // Default: Java
    tokenRegex = /(\/\/[^\n]*|\/\*[\s\S]*?\*\/)|("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|(@[a-zA-Z0-9_]+)|\b(abstract|assert|boolean|break|byte|case|catch|char|class|const|continue|default|do|double|else|enum|extends|final|finally|float|for|goto|if|implements|import|instanceof|int|interface|long|native|new|package|private|protected|public|return|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|void|volatile|while|record|yield|var|permits|sealed|non-sealed|true|false|null)\b|\b(String|Integer|Long|Double|Float|Boolean|Character|Byte|Short|Object|Math|System|Arrays|Collections|List|ArrayList|LinkedList|Set|HashSet|TreeSet|Map|HashMap|TreeMap|Queue|Deque|ArrayDeque|PriorityQueue|Stack|StringBuilder|StringBuffer|Comparator|Comparable|Iterator|Optional|Scanner|Exception|RuntimeException|Solution|TreeNode|ListNode|Node)\b|\b(0x[0-9a-fA-F]+|0b[01]+|\d+(?:\.\d+)?(?:[fFdDlL])?)\b|([a-zA-Z_$][a-zA-Z0-9_$]*)(?=\s*\()/g;
  }

  let result = "";
  let lastIndex = 0;
  let match;

  while ((match = tokenRegex.exec(code)) !== null) {
    if (match.index > lastIndex) {
      result += escapeHtml(code.slice(lastIndex, match.index));
    }
    const [full, comment, string, annotation, keyword, type, number, func] = match;
    if (comment) {
      result += `<span class="tok-comment">${escapeHtml(comment)}</span>`;
    } else if (string) {
      result += `<span class="tok-string">${escapeHtml(string)}</span>`;
    } else if (annotation) {
      result += `<span class="tok-annotation">${escapeHtml(annotation)}</span>`;
    } else if (keyword) {
      result += `<span class="tok-keyword">${escapeHtml(keyword)}</span>`;
    } else if (type) {
      result += `<span class="tok-type">${escapeHtml(type)}</span>`;
    } else if (number) {
      result += `<span class="tok-number">${escapeHtml(number)}</span>`;
    } else if (func) {
      result += `<span class="tok-function">${escapeHtml(func)}</span>`;
    }
    lastIndex = tokenRegex.lastIndex;
  }
  if (lastIndex < code.length) {
    result += escapeHtml(code.slice(lastIndex));
  }

  // Format into numbered lines
  const lines = result.split("\n");
  return lines
    .map(
      (line, i) =>
        `<div class="tok-line"><span class="line-num">${i + 1}</span><span class="line-code">${line || " "}</span></div>`
    )
    .join("");
}

/* --- App Messages & State --- */

function displayMessage(message, isError = false) {
  elements.appMessage.textContent = message;
  elements.appMessage.classList.toggle("is-error", isError);
}

function getProgress(card) {
  return progress[card.id] || null;
}

function isDue(card, now = Date.now()) {
  const state = getProgress(card);
  return !state || !state.dueAt || state.dueAt <= now;
}

function isMastered(card) {
  const state = getProgress(card);
  return state && (state.rating === "good" || state.rating === "easy") && (state.streak || 0) >= 1;
}

function isLearning(card) {
  const state = getProgress(card);
  return state && !isMastered(card);
}

function todayKey(timestamp = Date.now()) {
  const date = new Date(timestamp);
  return `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`;
}

function updateSummary() {
  const now = Date.now();
  const total = cards.length || 1;
  const due = cards.filter((card) => isDue(card, now)).length;
  const reviewedToday = Object.values(progress).filter(
    (state) => state.lastReviewedAt && todayKey(state.lastReviewedAt) === todayKey(now)
  ).length;
  const mastered = cards.filter(isMastered).length;
  const learning = cards.filter(isLearning).length;

  elements.dueCount.textContent = due;
  elements.reviewedCount.textContent = reviewedToday;
  elements.masteredCount.textContent = mastered;
  elements.problemCount.textContent = cards.length;

  const masteredPct = Math.round((mastered / total) * 100);
  const learningPct = Math.round((learning / total) * 100);

  elements.barMastered.style.width = `${masteredPct}%`;
  elements.barLearning.style.width = `${learningPct}%`;
}

function populateFilterOptions() {
  // Collections
  const groups = [...new Set(cards.flatMap((card) => card.groups || []))].sort((a, b) => a.localeCompare(b));
  for (const group of groups) {
    const opt = document.createElement("option");
    opt.value = group;
    opt.textContent = group;
    elements.groupFilter.append(opt);
  }

  // Topics
  const topics = [...new Set(cards.map((card) => card.topic).filter(Boolean))].sort((a, b) => a.localeCompare(b));
  for (const topic of topics) {
    const opt = document.createElement("option");
    opt.value = topic;
    opt.textContent = topic;
    elements.topicFilter.append(opt);
  }
}

function matchesFilters(card) {
  const query = elements.searchInput.value.trim().toLowerCase();
  if (query) {
    const haystack = [
      card.title,
      card.folder,
      card.prompt,
      card.topic,
      card.pattern,
      card.difficulty,
      card.frequentlyAsked ? "frequently asked top high frequency hot flame" : "",
      card.problemNumberFormatted,
      `#${card.problemNumber}`,
      card.lcNumber ? `lc ${card.lcNumber}` : "",
      card.lcTitle || "",
      ...(card.groups || [])
    ].join(" ").toLowerCase();
    if (!haystack.includes(query)) return false;
  }

  if (elements.groupFilter.value && !(card.groups || []).includes(elements.groupFilter.value)) return false;
  if (elements.topicFilter.value && card.topic !== elements.topicFilter.value) return false;
  if (elements.difficultyFilter.value && card.difficulty !== elements.difficultyFilter.value) return false;

  switch (elements.statusFilter.value) {
    case "frequently-asked":
      return Boolean(card.frequentlyAsked);
    case "due":
      return isDue(card);
    case "new":
      return !getProgress(card);
    case "mastered":
      return isMastered(card);
    default:
      return true;
  }
}

function getDiffDotClass(difficulty) {
  const d = String(difficulty || "").toLowerCase();
  if (d === "easy") return "row-diff-dot diff-easy";
  if (d === "hard") return "row-diff-dot diff-hard";
  return "row-diff-dot diff-medium";
}

function rowStatusClass(card) {
  const state = getProgress(card);
  if (!state) return "row-status";
  if (isDue(card)) return "row-status is-due";
  return "row-status is-good";
}

function renderList() {
  visibleCards = cards.filter(matchesFilters);
  elements.problemList.replaceChildren();
  elements.emptyList.hidden = visibleCards.length > 0;
  elements.resultsLabel.textContent = `${visibleCards.length} ${visibleCards.length === 1 ? "problem" : "problems"}`;

  for (const card of visibleCards) {
    const button = document.createElement("button");
    button.className = "problem-row";
    button.type = "button";
    button.setAttribute("aria-current", card.id === activeId ? "true" : "false");

    const num = card.problemNumberFormatted || `#${card.problemNumber || ""}`;
    const diff = card.difficulty || "Medium";
    const freqMarker = card.frequentlyAsked ? `<span class="row-freq-badge" title="🔥 High Frequency / Top Asked">🔥</span>` : "";

    button.innerHTML = `
      <span class="row-main">
        <span class="row-header">
          <span class="${getDiffDotClass(diff)}" title="${escapeHtml(diff)}"></span>
          <span class="row-num">${escapeHtml(num)}</span>
          <span class="row-title">${escapeHtml(card.title)}</span>
          ${freqMarker}
        </span>
        <span class="row-meta">${escapeHtml(card.pattern || card.topic || "Problem")}</span>
      </span>
      <span class="${rowStatusClass(card)}" aria-label="${isDue(card) ? "Due" : getProgress(card) ? "Scheduled" : "New"}"></span>
    `;

    button.addEventListener("click", () => selectCard(card.id));
    elements.problemList.append(button);
  }
  updateSummary();
}

function answerSection(title, value, isTrick = false, isSpan2 = false) {
  const hasNote = Boolean(value && String(value).trim());
  const content = hasNote
    ? safeNoteHtml(value)
    : `<p class="missing-note">Add notes for ${escapeHtml(title)} in REVISION.md.</p>`;
  const trickClass = isTrick ? " is-trick" : "";
  const spanClass = isSpan2 ? " is-span-2" : "";
  return `<section class="answer-section${trickClass}${spanClass}"><h3>${escapeHtml(title)}</h3>${content}</section>`;
}

function reviewLabel(card) {
  const state = getProgress(card);
  if (!state) return "New card";
  if (isDue(card)) return "Due now";
  const date = new Date(state.dueAt);
  return `Next review ${date.toLocaleDateString(undefined, { month: "short", day: "numeric" })}`;
}

function encodedPath(path) {
  return path.split("/").map(encodeURIComponent).join("/");
}

function localFileUrl(path) {
  return `../${encodedPath(path)}`;
}

function updateHintsUI(card) {
  const hints = card.hints || [];
  revealedHintCount = 0;
  elements.hintsStack.replaceChildren();

  if (!hints.length) {
    elements.hintsDrawer.hidden = true;
    return;
  }

  elements.hintsDrawer.hidden = false;
  elements.hintsBody.hidden = true;
  elements.nextHintButton.hidden = true;
  elements.hintBtnLabel.textContent = `Need a hint? (${hints.length} available) [H]`;
  elements.hintCounter.textContent = "";
}

function revealNextHint(card) {
  const hints = card.hints || [];
  if (!hints.length) return;

  if (elements.hintsBody.hidden) {
    elements.hintsBody.hidden = false;
  }

  if (revealedHintCount < hints.length) {
    const hintText = hints[revealedHintCount];
    const item = document.createElement("div");
    item.className = "hint-item";
    item.innerHTML = `<span class="hint-item-label">Hint ${revealedHintCount + 1}:</span> ${formatInline(hintText)}`;
    elements.hintsStack.append(item);
    revealedHintCount += 1;
  }

  elements.hintCounter.textContent = `${revealedHintCount} / ${hints.length} revealed`;
  elements.hintBtnLabel.textContent = "Hints unfolded";

  if (revealedHintCount < hints.length) {
    elements.nextHintButton.hidden = false;
    elements.nextHintButton.textContent = `Show hint ${revealedHintCount + 1} of ${hints.length} ↓`;
  } else {
    elements.nextHintButton.hidden = true;
  }
}

function toggleHints(card) {
  const hints = card.hints || [];
  if (!hints.length) return;

  if (elements.hintsBody.hidden || revealedHintCount === 0) {
    revealNextHint(card);
  } else {
    elements.hintsBody.hidden = true;
    elements.hintBtnLabel.textContent = `Show hints (${revealedHintCount}/${hints.length} seen) [H]`;
  }
}

/* --- Markdown Preview Modal --- */

async function openMarkdownModal(filePath, title, rawUrl) {
  elements.modalTitle.textContent = title || "Document Preview";
  elements.modalRawLink.href = rawUrl || filePath;
  elements.modalBody.innerHTML = "<p>Loading document preview...</p>";
  elements.markdownModal.hidden = false;

  try {
    const response = await fetch(filePath);
    if (!response.ok) throw new Error(`Could not load document (${response.status}).`);
    const rawMd = await response.text();
    elements.modalBody.innerHTML = renderMarkdownToHtml(rawMd);
  } catch (err) {
    elements.modalBody.innerHTML = `<p class="app-message is-error">Failed to load preview: ${escapeHtml(err.message)}</p>`;
  }
}

function closeMarkdownModal() {
  elements.markdownModal.hidden = true;
}

function renderCard() {
  const card = cards.find((item) => item.id === activeId) || visibleCards[0] || cards[0];
  if (!card) return;
  activeId = card.id;

  elements.flashCard.dataset.cardId = card.id;
  elements.cardNumber.textContent = card.problemNumberFormatted || `#${card.problemNumber || ""}`;
  elements.cardTitle.textContent = card.title;
  elements.cardPrompt.textContent = card.prompt || "No prompt available. Review the problem statement in REVISION.md.";
  elements.breadcrumb.textContent = (card.groups || []).join("  /  ") || "Other problems";
  elements.reviewState.textContent = reviewLabel(card);

  // Difficulty pill
  const diff = card.difficulty || "Medium";
  elements.cardDifficulty.textContent = diff;
  elements.cardDifficulty.className = `difficulty-pill is-${diff.toLowerCase()}`;

  // Frequently asked pill
  if (card.frequentlyAsked) {
    elements.cardFreqPill.hidden = false;
  } else {
    elements.cardFreqPill.hidden = true;
  }

  // Topic and Pattern
  elements.cardTopic.textContent = card.topic || "General";
  elements.cardPattern.textContent = card.pattern || "Pattern";

  // LeetCode Pill
  if (card.lcUrl) {
    elements.cardLcPill.hidden = false;
    elements.cardLcPill.href = card.lcUrl;
    elements.cardLcText.textContent = card.lcNumber ? `LC #${card.lcNumber} ↗` : "LeetCode ↗";
    elements.lcTopLink.hidden = false;
    elements.lcTopLink.href = card.lcUrl;
  } else {
    elements.cardLcPill.hidden = true;
    elements.lcTopLink.hidden = true;
  }

  // Answer Grid
  elements.answerGrid.innerHTML = [
    answerSection("Core Idea & Approach", card.notes?.concept, false, true),
    answerSection("Pattern & Technique", card.notes?.pattern),
    answerSection("Key Trick & Invariant", card.notes?.trick, true),
    answerSection("Time & Space Complexity", card.notes?.complexity),
    answerSection("Edge Cases Checklist", card.notes?.edgeCases)
  ].join("");

  // README links (Formatted Preview Modal + Raw Link)
  const readmePath = card.readme || `problems/${card.folder}/README.md`;
  elements.readmeRawLink.href = localFileUrl(readmePath);

  // Position
  const activeIdx = Math.max(visibleCards.findIndex((item) => item.id === activeId), 0);
  elements.cardPosition.textContent = `Problem ${activeIdx + 1} of ${visibleCards.length || cards.length}`;

  // Reset answer reveal state
  elements.answer.hidden = true;
  elements.revealButton.hidden = false;
  elements.revealButton.textContent = "Reveal the approach ↓";

  // Reset code
  codeRevealed = false;
  elements.codeContainer.hidden = true;
  elements.languageSelect.hidden = true;
  elements.languageSelect.replaceChildren();
  elements.copyCodeButton.hidden = true;
  elements.sourceCode.innerHTML = "";
  elements.codeRevealButton.hidden = false;
  elements.codeCaption.textContent = "Try to write the solution before opening the reference.";

  for (const source of card.sources) {
    const option = document.createElement("option");
    option.value = source.path;
    option.textContent = `${source.language} · ${source.filename}`;
    elements.languageSelect.append(option);
  }

  const preferred =
    card.sources.find((source) => source.language === "Java") ||
    card.sources.find((source) => source.language === "Python") ||
    card.sources[0];
  if (preferred) elements.languageSelect.value = preferred.path;

  // Progressive Hints
  updateHintsUI(card);

  history.replaceState(null, "", `#${encodeURIComponent(card.id)}`);
  renderList();
}

function selectCard(id) {
  if (!cards.some((card) => card.id === id)) return;
  activeId = id;
  renderCard();
}

function moveCard(direction) {
  if (!visibleCards.length) return;
  const index = visibleCards.findIndex((card) => card.id === activeId);
  const next = (index + direction + visibleCards.length) % visibleCards.length;
  selectCard(visibleCards[next].id);
}

async function loadSourceCode() {
  const card = cards.find((item) => item.id === activeId);
  const source = card?.sources.find((item) => item.path === elements.languageSelect.value);
  if (!source) return;
  elements.sourceCode.textContent = "Loading solution…";
  try {
    const response = await fetch(localFileUrl(source.path));
    if (!response.ok) throw new Error(`Could not load ${source.filename} (${response.status}).`);
    rawLoadedCode = await response.text();
    elements.sourceCode.innerHTML = highlightSyntax(rawLoadedCode, source.language);
    elements.codeCaption.textContent = `${source.language} · ${source.filename} (${rawLoadedCode.split("\n").length} lines)`;
    elements.copyCodeButton.hidden = false;
  } catch (error) {
    rawLoadedCode = "";
    elements.sourceCode.textContent = "Solution could not be loaded.";
    elements.codeCaption.textContent = error.message;
    elements.copyCodeButton.hidden = true;
    displayMessage(error.message, true);
  }
}

function revealCode() {
  if (!codeRevealed) {
    codeRevealed = true;
    elements.codeRevealButton.hidden = true;
    elements.languageSelect.hidden = false;
    elements.codeContainer.hidden = false;
  }
  loadSourceCode();
}

async function copyCodeToClipboard() {
  if (!rawLoadedCode) return;
  try {
    await navigator.clipboard.writeText(rawLoadedCode);
    elements.copyLabel.textContent = "Copied! ✓";
    elements.copyCodeButton.classList.add("copied");
    setTimeout(() => {
      elements.copyLabel.textContent = "Copy code";
      elements.copyCodeButton.classList.remove("copied");
    }, 2000);
  } catch {
    displayMessage("Clipboard copy failed.", true);
  }
}

function saveProgress() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
    return true;
  } catch (error) {
    displayMessage(`Could not save review progress: ${error.message}`, true);
    return false;
  }
}

function rateCard(rating) {
  const card = cards.find((item) => item.id === activeId);
  if (!card) return;
  const now = Date.now();
  const old = getProgress(card);
  const oldInterval = Number(old?.intervalDays) || 0;
  let intervalDays;
  if (rating === "again") intervalDays = 10 / (24 * 60);
  else if (rating === "hard") intervalDays = oldInterval ? Math.max(1, oldInterval * 1.25) : 1;
  else if (rating === "easy") intervalDays = oldInterval ? Math.max(4, oldInterval * 2.5) : 4;
  else intervalDays = oldInterval ? Math.max(3, oldInterval * 2) : 1;

  progress[card.id] = {
    intervalDays,
    dueAt: now + intervalDays * DAY,
    lastReviewedAt: now,
    rating,
    streak: rating === "again" ? 0 : (old?.streak || 0) + 1
  };
  const didSave = saveProgress();
  renderCard();
  displayMessage(
    didSave
      ? `${card.title} scheduled for review in ${intervalDays >= 1 ? Math.round(intervalDays) + " days" : "10 minutes"}.`
      : "Review updated for this session."
  );
  if (elements.statusFilter.value === "due" && !isDue(card)) moveCard(1);
}

function startSurpriseReview() {
  const candidatePool = visibleCards.filter((card) => isDue(card));
  const pool = candidatePool.length ? candidatePool : visibleCards;
  if (!pool.length) {
    displayMessage("No cards match the current filters.", true);
    return;
  }
  const candidate = pool[Math.floor(Math.random() * pool.length)];
  selectCard(candidate.id);
  displayMessage(candidatePool.length ? "A due card, picked at random." : "A random card from this selection.");
}

function parseInitialHash() {
  if (!location.hash) return null;
  try {
    return decodeURIComponent(location.hash.slice(1));
  } catch {
    return null;
  }
}

function loadSavedProgress() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    progress = saved ? JSON.parse(saved) : {};
    if (!progress || typeof progress !== "object" || Array.isArray(progress)) progress = {};
  } catch (error) {
    progress = {};
    displayMessage(`Saved progress could not be read: ${error.message}`, true);
  }
}

function bindEvents() {
  const reFilter = () => {
    renderList();
    if (!visibleCards.some((card) => card.id === activeId) && visibleCards[0]) {
      selectCard(visibleCards[0].id);
    } else {
      renderCard();
    }
  };

  elements.searchInput.addEventListener("input", reFilter);
  elements.groupFilter.addEventListener("change", reFilter);
  elements.topicFilter.addEventListener("change", reFilter);
  elements.difficultyFilter.addEventListener("change", reFilter);
  elements.statusFilter.addEventListener("change", reFilter);

  elements.revealButton.addEventListener("click", () => {
    elements.answer.hidden = false;
    elements.revealButton.hidden = true;
    elements.languageSelect.hidden = true;
  });

  elements.codeRevealButton.addEventListener("click", revealCode);
  elements.copyCodeButton.addEventListener("click", copyCodeToClipboard);
  elements.languageSelect.addEventListener("change", loadSourceCode);

  elements.hintToggleButton.addEventListener("click", () => {
    const card = cards.find((item) => item.id === activeId);
    if (card) toggleHints(card);
  });

  elements.nextHintButton.addEventListener("click", () => {
    const card = cards.find((item) => item.id === activeId);
    if (card) revealNextHint(card);
  });

  elements.nextButton.addEventListener("click", () => moveCard(1));
  elements.previousButton.addEventListener("click", () => moveCard(-1));
  elements.shuffleButton.addEventListener("click", startSurpriseReview);

  // Markdown Modal Openers
  elements.readmeModalBtn.addEventListener("click", () => {
    const card = cards.find((item) => item.id === activeId);
    if (!card) return;
    const path = card.readme || `problems/${card.folder}/README.md`;
    openMarkdownModal(localFileUrl(path), `${card.title} — Problem Statement`, localFileUrl(path));
  });

  elements.repoReadmeBtn.addEventListener("click", () => {
    openMarkdownModal("../README.md", "Repository Problem Guide", "../README.md");
  });

  elements.modalCloseBtn.addEventListener("click", closeMarkdownModal);
  elements.markdownModal.addEventListener("click", (e) => {
    if (e.target === elements.markdownModal) closeMarkdownModal();
  });

  document.querySelectorAll("[data-rating]").forEach((button) => {
    button.addEventListener("click", () => rateCard(button.dataset.rating));
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !elements.markdownModal.hidden) {
      closeMarkdownModal();
      return;
    }

    const target = event.target;
    if (target instanceof HTMLInputElement || target instanceof HTMLSelectElement || target instanceof HTMLTextAreaElement) {
      if (event.key === "/" && target !== elements.searchInput) {
        event.preventDefault();
        elements.searchInput.focus();
      }
      return;
    }

    if (target instanceof HTMLButtonElement && event.code === "Space") return;

    if (event.key === "ArrowRight") {
      moveCard(1);
    } else if (event.key === "ArrowLeft") {
      moveCard(-1);
    } else if (event.code === "Space") {
      event.preventDefault();
      if (elements.answer.hidden) {
        elements.revealButton.click();
      } else {
        revealCode();
      }
    } else if (event.key === "h" || event.key === "H") {
      event.preventDefault();
      const card = cards.find((item) => item.id === activeId);
      if (card) toggleHints(card);
    } else if (event.key === "c" || event.key === "C") {
      event.preventDefault();
      revealCode();
    } else if (event.key === "1") {
      rateCard("again");
    } else if (event.key === "2") {
      rateCard("hard");
    } else if (event.key === "3") {
      rateCard("good");
    } else if (event.key === "4") {
      rateCard("easy");
    } else if (event.key === "/" && !elements.markdownModal.hidden) {
      return;
    } else if (event.key === "/") {
      event.preventDefault();
      elements.searchInput.focus();
    } else if (event.key === "t" || event.key === "T") {
      event.preventDefault();
      toggleTheme();
    }
  });

  elements.themeToggleBtn?.addEventListener("click", toggleTheme);

  if (window.matchMedia) {
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (e) => {
      try {
        if (!localStorage.getItem(THEME_KEY)) {
          applyTheme(e.matches ? "dark" : "light");
        }
      } catch {}
    });
  }
}

async function start() {
  try {
    const response = await fetch("./catalog.json", { cache: "no-store" });
    if (!response.ok) throw new Error("Study catalog is missing. Run `python3 revision/build_catalog.py`.");
    const catalog = await response.json();
    cards = catalog.cards || [];
    if (!cards.length) throw new Error("The catalog has no problem cards yet.");
    loadSavedProgress();
    populateFilterOptions();
    bindEvents();
    const requestedId = parseInitialHash();
    activeId = cards.some((card) => card.id === requestedId) ? requestedId : cards[0].id;
    renderList();
    renderCard();
    displayMessage(`Deck ready: ${cards.length} problems across ${catalog.groups?.length || 0} collections.`);
  } catch (error) {
    elements.cardTitle.textContent = "Cards are not ready yet";
    elements.cardPrompt.textContent = error.message;
    elements.revealButton.hidden = true;
    elements.problemList.replaceChildren();
    elements.emptyList.hidden = false;
    elements.emptyList.textContent = "Build the catalog with `python3 revision/build_catalog.py`, then refresh.";
    displayMessage(error.message, true);
  }
}

start();
