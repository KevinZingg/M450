import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    Calculator calculator = new Calculator();

    @org.junit.jupiter.api.Test
    void add() {
        assertEquals(5.0, calculator.add(2.0, 3.0));
        assertEquals(0.0, calculator.add(-2.0, 2.0));
        assertEquals(-5.0, calculator.add(-2.0, -3.0));
    }

    @org.junit.jupiter.api.Test
    void subtract() {
        assertEquals(-1.0, calculator.subtract(2.0, 3.0));
        assertEquals(0.0, calculator.subtract(2.0, 2.0));
        assertEquals(1.0, calculator.subtract(3.0, 2.0));
    }

    @org.junit.jupiter.api.Test
    void multiply() {
        assertEquals(6.0, calculator.multiply(2.0, 3.0));
        assertEquals(0.0, calculator.multiply(0.0, 3.0));
        assertEquals(-6.0, calculator.multiply(-2.0, 3.0));
    }

    @org.junit.jupiter.api.Test
    void divide() {
        assertEquals(2.0, calculator.divide(6.0, 3.0));
        assertEquals(0.0, calculator.divide(0.0, 3.0));

        // Test for dividing by zero
        assertThrows(ArithmeticException.class, () -> {
            calculator.divide(1.0, 0.0);
        });
    }
}
