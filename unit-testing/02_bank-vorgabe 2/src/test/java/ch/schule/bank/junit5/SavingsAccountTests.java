package ch.schule.bank.junit5;

import ch.schule.SavingsAccount;



/**
 * Tests f�r die Klasse SavingsAccount.
 *
 * @author Roger H. J&ouml;rg
 * @version 1.0
 */

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;


/**
 * Tests für die Klasse SavingsAccount.
 *
 * @author XXX
 * @version 1.0
 */
public class SavingsAccountTests
{
	@Test
	public void testWithdrawal() {
		SavingsAccount account = new SavingsAccount("testID");
		account.deposit(2025, 1000);

		boolean isWithdrawn = account.withdraw(2025, 500);
		assertTrue(isWithdrawn, "Withdrawal should be successful.");

		isWithdrawn = account.withdraw(2025, 600);
		assertFalse(isWithdrawn, "Withdrawal should fail due to insufficient balance.");
	}
}

