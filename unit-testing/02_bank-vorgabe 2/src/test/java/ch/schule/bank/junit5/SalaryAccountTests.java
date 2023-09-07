package ch.schule.bank.junit5;

import ch.schule.SalaryAccount;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;


/**
 * Tests der Klasse SalaryAccount.
 *
 * @author XXX
 * @version 1.1
 */
public class SalaryAccountTests
{
	/**
	 * Der Test.
	 */
	@Test
	public void testSuccessfulWithdraw() {
		SalaryAccount account = new SalaryAccount("testID", -5000);

		account.deposit(2025, 1000);

		boolean withdrawSuccessful = account.withdraw(2025, 1000);

		assertTrue(withdrawSuccessful, "Withdrawal should be successful.");
		assertEquals(0, account.getBalance(), "Balance should be 0 after withdrawing 1000.");
	}
}
