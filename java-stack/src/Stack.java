public class Stack {

    private static final int FIRST_INDEX = -1;

    private int top;
    private int data[];
    private int max_stack;

    public int Top() {
        return this.top;
    }

    private void Top(int top) {
        this.top = top;
    }

    private int Data(int index) {
        return this.data[index];
    }

    private void Data(int index, int item) {
        this.data[index] = item;
    }

    public int Max() {
        return this.max_stack;
    }

    private void Max(int max) {
        this.max_stack = max;
    }

    public Stack(int items) {
        this.Max(items);
        this.data = new int[this.Max()];
        this.Top(Stack.FIRST_INDEX);
    }

    public boolean IsEmpty() {
        return this.Top() == Stack.FIRST_INDEX;
    }

    public boolean IsFull() {
        return this.Top() == (this.Max() - 1);
    }

    public void Push(int item) throws Exception {
        if (this.IsFull())
            throw new Exception("Stack is full.");

        this.Top(this.IncrementTop());
        this.Data(this.Top(), item);
    }

    public int Pop() throws Exception {
        if (this.IsEmpty())
            throw new Exception("Stack is empty.");

        int item = this.Data(this.Top());
        this.Top(this.DecrementTop());

        return item;
    }

    private int IncrementTop()
    {
        return this.Top() + 1;
    }

    private int DecrementTop()
    {
        return this.Top() - 1;
    }

}
