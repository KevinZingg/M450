package ch.schule.bank.junit5;

import ch.schule.PromoYouthSavingsAccount;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class PromoYouthSavingsAccountTests {

	/**
	 * Tests the deposit method with bonus.
	 */
	@Test
	public void testDepositWithBonus() {
		PromoYouthSavingsAccount account = new PromoYouthSavingsAccount("testID");

		boolean depositSuccessful = account.deposit(2025, 1000);  // 1000 millirappen

		assertTrue(depositSuccessful, "Deposit should be successful.");

		assertEquals(1010, account.getBalance(), "Balance should be 1010 millirappen after depositing 1000 with 1% bonus.");
	}
}
