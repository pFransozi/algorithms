
package DataStructure;

public class CircularQueue {

    private static final int EMPTY_INDEX = -1;
    private int front, rear;
    private int data[];
    private int current_size;

    public int Front() {
        return this.front;
    }

    private void Front(int front) {
        this.front = front;
    }

    public int Rear() {
        return this.rear;
    }

    public void Rear(int rear) {
        this.rear = rear;
    }

    private void Data(int data, int index) {
        this.data[index] = data;
    }

    private int Data(int index) {
        return this.data[index];
    }

    private int CurrentSize() {
        return this.current_size;
    }

    private void CurrentSize(int current_size) {
        this.current_size = current_size;
    }

    public int Size() {
        return this.data.length;
    }

    public CircularQueue(int size) {

        this.data = new int[size];
        this.Front(CircularQueue.EMPTY_INDEX);
        this.Rear(CircularQueue.EMPTY_INDEX);
        this.CurrentSize(0);

    }

    public boolean IsEmpty() {
        return (this.CurrentSize() == 0);
    }

    public boolean IsFull() {
        return (this.CurrentSize() == this.Size());
    }

    public void Enqueue(int new_element) throws Exception {

        if (this.IsFull())
            throw new Exception("Queue is full.");

        int new_rear_index = (this.Rear() + 1) % this.Size();
        this.Rear(new_rear_index);
        this.Data(new_element, new_rear_index);
        this.CurrentSize(this.CurrentSize() + 1);

        if (this.Front() == CircularQueue.EMPTY_INDEX)
            this.Front(this.Rear());

    }

    public int Dequeue() throws Exception {
        if (this.IsEmpty())
            throw new Exception("Queue is empty");

        int element_dequeued = this.Data(this.Front());
        int new_front_index = (this.Front() + 1) % this.Size();
        this.Front(new_front_index);
        this.CurrentSize(this.CurrentSize() - 1);

        if (this.CurrentSize() == 0) {
            this.Front(CircularQueue.EMPTY_INDEX);
            this.Rear(CircularQueue.EMPTY_INDEX);
        }

        return element_dequeued;

    }

    public int Peek() throws Exception {
        if (this.IsEmpty())
            throw new Exception("Queue is empty");

        return this.Data(this.Front());
    }

    public String Print() {
        if (this.IsEmpty())
            return "";

        StringBuilder s_builder = new StringBuilder();

        int current_index = this.Front();
        do {
            s_builder.append(this.Data(current_index) + ", ");

            if (current_index == this.Rear())
                break;

            current_index = (current_index + 1) % this.Size();
        } while (current_index != this.Front());

        return s_builder.toString().substring(0, s_builder.length() - 2);
    }
}
