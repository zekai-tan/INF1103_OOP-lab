class Supplier:

    def __init__(
        self,
        supplier_id: str,
        name: str,
        contact_email: str
    ) -> None:
        #remove leading/trailing spaces and standardise the supplier ID
        supplier_id = supplier_id.strip().upper()
        name = name.strip()
        contact_email = contact_email.strip()

        #supplier details cannot be empty
        if not supplier_id or not name or not contact_email:
            raise ValueError("Supplier details cannot be empty.")

        #store the supplier attributes
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    def display_information(self) -> None:
        #display the supplier information
        print(
            f"Supplier ID: {self.__supplier_id} | "
            f"Name: {self.__name} | "
            f"Contact Email: {self.__contact_email}"
        )

    def to_dict(self) -> dict[str, str]:
        #convert supplier information into a dictionary for JSON saving
        return {
            "supplier_id": self.__supplier_id,
            "supplier_name": self.__name,
            "supplier_email": self.__contact_email
        }