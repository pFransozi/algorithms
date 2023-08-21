import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class TestStack {

    private Stack stack;

    @Before
    public void InitializeStack() {
        stack = new Stack(3);
    }

    @Test
    public void IsEmpty() {

        int FIRST_INDEX = -1;

        assertTrue(stack.IsEmpty());
        assertEquals(FIRST_INDEX, stack.Top());
    }

    @Test(expected = Exception.class)
    public void PopAnEmptyStack() throws Exception {
        stack.Pop();
    }

    @Test(expected = Exception.class)
    public void PushMoreThanMax() throws Exception {

        for (int i = 0; i < stack.Max() + 2; i++) {
            stack.Push(0);
        }
    }

    @Test
    public void PushOneItem() throws Exception {
        stack.Push(0);

        assertFalse(stack.IsEmpty());
        assertEquals(0, stack.Top());
    }

    @Test
    public void PushAtTop() throws Exception {
        for (int i = 0; i < stack.Max(); i++) {
            stack.Push(i);
        }

        assertFalse(stack.IsEmpty());
        assertEquals(stack.Max() - 1, stack.Top());
    }

}
