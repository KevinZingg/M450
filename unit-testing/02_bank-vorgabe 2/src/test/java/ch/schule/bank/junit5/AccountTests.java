package ch.schule.bank.junit5;

import ch.schule.Account;
import ch.schule.SalaryAccount;
import ch.schule.SavingsAccount;
import org.junit.jupiter.api.Test;


import java.util.TreeMap;

import static org.junit.jupiter.api.Assertions.*;


/**
 * Tests für die Klasse Account.
 *
 * @author xxxx
 * @version 1.0
 */
public class AccountTests {
    /**
     * Tested die Initialisierung eines Kontos.
     */
    /**
     * Tested die Initialisierung eines Kontos.
     */
    @Test
    public void testInit() {
        String expectedId = "test123";
        Account testAccount = new SavingsAccount(expectedId);  // Assuming SavingsAccount is a concrete subclass of Account

        assertEquals(expectedId, testAccount.getId(), "Account ID mismatch!");
        assertEquals(0, testAccount.getBalance(), "Initial account balance should be 0!");
    }


    /**
     * Testet das Einzahlen auf ein Konto.
     */
    @Test
    public void testDeposit() {
        // Initialize a new Account
        Account testAccount = new SavingsAccount("test123");

        // Deposit an amount to the account
        long depositAmount = 1000;
        testAccount.deposit(20230907, depositAmount);

        // Check if the balance matches the deposited amount
        assertEquals(depositAmount, testAccount.getBalance());
    }
    /**
     * Testet das Abheben von einem Konto.
     */
    @Test
    public void testWithdraw(){
        // Initialize a new Account
        Account testAccount = new SavingsAccount("test123");

        // Deposit an amount to the account
        long depositAmount = 1000;
        testAccount.deposit(20230907, depositAmount);

        // Add an amount to the account
        long withdrawnAmount = 500;
        testAccount.withdraw(20230907, withdrawnAmount);

        // Check result
        assertEquals(depositAmount - withdrawnAmount, testAccount.getBalance(), "Gut!");

    }

    /**
     * Tests the reference from SavingsAccount
     */
    @Test
    public void testReferences() {
        fail("toDo");
    }

    /**
     * teste the canTransact Flag
     */
    @Test
    public void testCanTransact() {
        fail("toDo");
    }

    /**
     * Experimente mit print().
     */
    @Test
    public void testPrint() {
        fail("toDo");
    }

    /**
     * Experimente mit print(year,month).
     */
    @Test
    public void testMonthlyPrint() {
        fail("toDo");
    }

}
