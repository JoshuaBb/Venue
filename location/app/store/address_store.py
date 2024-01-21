from app.util.database import Db
from app.dto.address_dto import AddressDto
from typing import Optional
from app.model.address import AddressResponse


class AddressStore:

    def __init__(self, db: Db):
        self.db = db

    async def get_address_by_id(self, address_id: int) -> Optional[AddressDto]:
        """Gets the address info from the database using a address_id"""
        return await self.db.query_one("select * from address where address_id = %s", AddressDto, address_id)

    async def delete_address_by_id(self, address_id: int) -> int:
        """Deletes a address data from the database using the address_id"""
        return await self.db.update("delete from address where address_id = %s", address_id)

    # TODO: Change. This is a bit off to have the response come down to this layer
    async def insert_address(self, address: AddressResponse) -> int:
        """Inserts address data into the database"""
        insert_str = """
           insert into address 
             (address_line_one, 
              address_line_two, 
              address_line_three, 
              address_line_four, 
              city, 
              state_or_province, 
              zip_or_postal, 
              country_code, 
              latitude, 
              longitude, 
              place_id, 
              created_at
            ) 
           VALUES 
             (%s, 
             %s, 
             %s, 
             %s, 
             %s, 
             %s, 
             %s,
             %s,
             %s,
             %s,
             %s, 
             NOW()
            )"""
        return await self.db.update(
            insert_str,
            (address.address_line_one,
             address.address_line_two,
             address.address_line_three,
             address.address_line_four,
             address.city,
             address.state_or_province,
             address.zip_or_postal,
             address.country_code,
             address.latitude,
             address.longitude,
             address.place_id)
        )

    async def find_addresses(self) -> list[AddressDto]:
        return await self.db.query("select * from address", AddressDto)

