package ch.schule.bank.junit5;

import ch.schule.Booking;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;


/**
 * Tests für die Klasse Booking.
 *
 * @author Luigi Cavuoti
 * @version 1.1
 */
public class BookingTests
{
	/**
	 * Tests f�r die Erzeugung von Buchungen.
	 */
	@Test
	public void testInitialization() {
		Booking booking = new Booking(2025, 1000);

		assertEquals(2025, booking.getDate());
		assertEquals(1000, booking.getAmount());
	}
	/**
	 * Experimente mit print().
	 */
	@Test
	public void testPrint()
	{
		fail("toDo");
	}
}
