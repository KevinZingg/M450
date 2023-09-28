package ch.bbw.addressbook;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Arrays;
import java.util.List;

@SpringBootTest
class AddressbookApplicationTests {

	@Mock
	private AddressDAO_Database addressDAO; // Mock für d'AddressDAO_Database-Klass

	@InjectMocks
	private AddressService addressService; // AddressService isch d'Klass, wo d'AddressDAO_Database brucht

	@BeforeEach
	void setUp() {
		MockitoAnnotations.openMocks(this); // Initialisiert d'Mocks vor jedem Test
	}

	@Test
	void testReadAllAddresses() {
		// Macht en Mock für mehri Adressä
		Address address1 = new Address(1, "John", "Doe", "123456789", null);
		Address address2 = new Address(2, "Jane", "Doe", "987654321", null);
		Address address3 = new Address(3, "Alice", "Smith", "111222333", null);
		Address address4 = new Address(4, "Bob", "Johnson", "444555666", null);
		List<Address> mockAddresses = Arrays.asList(address1, address2, address3, address4);

		when(addressDAO.readAll()).thenReturn(mockAddresses); // Simuliert d'Verhalte vo readAll()

		// Nimmt a, dass es en Methode git im AddressService, wo addressDAO.readAll() brucht
		List<Address> retrievedAddresses = addressService.getAllAddresses();

		// Überprüeft, ob d'Listi d'richtigi Grössi het und ob d'Vornamä korrekt sind
		assertEquals(4, retrievedAddresses.size());
		assertEquals("John", retrievedAddresses.get(0).getFirstname());
		assertEquals("Jane", retrievedAddresses.get(1).getFirstname());
		assertEquals("Alice", retrievedAddresses.get(2).getFirstname());
		assertEquals("Bob", retrievedAddresses.get(3).getFirstname());
	}
}
