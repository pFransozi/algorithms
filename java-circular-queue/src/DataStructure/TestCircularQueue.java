package DataStructure;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class TestCircularQueue {

    private static final int ELEMENTS_SIZE = 3;
    private CircularQueue c_queue;

    private void EnqueueMaxElemetsSize(int max_elements_size) throws Exception {
        for (int index = 0; index < max_elements_size; index++) {
            c_queue.Enqueue(index);
        }
    }

    @Before
    public void InicializeQueue() {
        c_queue = new CircularQueue(TestCircularQueue.ELEMENTS_SIZE);
    }

    @Test
    public void IsEmpty() {
        assertTrue(this.c_queue.IsEmpty());
    }

    public void IsNotFull() {
        assertFalse(c_queue.IsFull());
    }

    @Test(expected = Exception.class)
    public void EnqueueMoreThanMaxElementsSize() throws Exception {
        for (int index = 0; index < (TestCircularQueue.ELEMENTS_SIZE + 1); index++) {
            c_queue.Enqueue(index);
        }
    }

    @Test(expected = Exception.class)
    public void DequeueAnEmptyQueue() throws Exception {
        c_queue.Dequeue();
    }

    @Test
    public void EnqueueMaxElemetsSize() throws Exception {
        this.EnqueueMaxElemetsSize(TestCircularQueue.ELEMENTS_SIZE);

        assertTrue(c_queue.IsFull());
        assertFalse(c_queue.IsEmpty());
        assertEquals(c_queue.Front(), 0);
        assertEquals(c_queue.Rear(), TestCircularQueue.ELEMENTS_SIZE - 1);
    }

    @Test
    public void EnqueueDequeueAllElements() throws Exception {
        this.EnqueueMaxElemetsSize(TestCircularQueue.ELEMENTS_SIZE);

        assertTrue(c_queue.IsFull());
        assertFalse(c_queue.IsEmpty());
        assertEquals(c_queue.Front(), 0);
        assertEquals(c_queue.Rear(), TestCircularQueue.ELEMENTS_SIZE - 1);

        for (int index = 0; index < TestCircularQueue.ELEMENTS_SIZE; index++) {
            assertEquals(c_queue.Dequeue(), index);
        }

        assertFalse(c_queue.IsFull());
        assertTrue(c_queue.IsEmpty());
        assertEquals(c_queue.Front(), -1);
        assertEquals(c_queue.Rear(), -1);
    }

    @Test
    public void EnqueueAllElementsDequeueOneEnqueueOne() throws Exception {
        this.EnqueueMaxElemetsSize(TestCircularQueue.ELEMENTS_SIZE);

        assertTrue(c_queue.IsFull());
        assertFalse(c_queue.IsEmpty());
        assertEquals(c_queue.Front(), 0);
        assertEquals(c_queue.Rear(), TestCircularQueue.ELEMENTS_SIZE - 1);

        int dequeued_element = c_queue.Dequeue();

        assertEquals(dequeued_element, 0);
        assertFalse(c_queue.IsFull());
        assertFalse(c_queue.IsEmpty());
        assertEquals(c_queue.Front(), 1);
        assertEquals(c_queue.Rear(), TestCircularQueue.ELEMENTS_SIZE - 1);

        c_queue.Enqueue(4);
        assertTrue(c_queue.IsFull());
        assertFalse(c_queue.IsEmpty());
        assertEquals(c_queue.Front(), 1);
        assertEquals(c_queue.Rear(), 0);

    }

    @Test
    public void Print() throws Exception {
        this.EnqueueMaxElemetsSize(TestCircularQueue.ELEMENTS_SIZE);

        String printed = c_queue.Print();

        assertEquals(printed, "0, 1, 2");
    }

}
