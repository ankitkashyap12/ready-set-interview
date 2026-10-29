import java.util.HashMap;
import java.util.Map;

class LRUCache {

    int capacity;

    static class DoubleLinkedList {
        int key;
        int value;
        DoubleLinkedList next;
        DoubleLinkedList prev;

        DoubleLinkedList(int key, int val) {
            this.key = key;
            this.value = val;
            this.next = null;
            this.prev = null;
        }
    }

    private Map<Integer, DoubleLinkedList> cacheMap;
    DoubleLinkedList head;
    DoubleLinkedList tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        cacheMap = new HashMap<>();
        head = new DoubleLinkedList(0, 0);
        tail = new DoubleLinkedList(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        DoubleLinkedList node = cacheMap.get(key);
        if (node == null)
            return -1;
        // Detach and move to front (most recently used)
        removeNode(node);
        moveToFront(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        DoubleLinkedList node = cacheMap.get(key);
        if (node == null) {
            DoubleLinkedList newNode = new DoubleLinkedList(key, value);
            cacheMap.put(key, newNode);
            moveToFront(newNode);
            if (cacheMap.size() > capacity) {
                // Evict node before dummy tail (least recently used)
                DoubleLinkedList lruNode = popTail();
                cacheMap.remove(lruNode.key);
            }
        } else {
            removeNode(node);
            node.value = value;
            moveToFront(node);
        }
    }

    public void removeNode(DoubleLinkedList node) {
        DoubleLinkedList prevNode = node.prev;
        DoubleLinkedList nextNode = node.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
    }

    public void moveToFront(DoubleLinkedList node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }

    public DoubleLinkedList popTail() {
        DoubleLinkedList lruNode = tail.prev;
        removeNode(lruNode);
        return lruNode;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */