import unittest
import pytest
import asyncio
from unittest.mock import patch
from app.store.address_store import AddressStore
from app.dto.address_dto import AddressDto, address_dto_from_dict
from app.util.database import Db
from mockito import when


class AddressStoreTest(unittest.IsolatedAsyncioTestCase):

    @patch('app.util.database.Db')
    @pytest.mark.asyncio
    async def test_delete_address_by_id(self, db: Db):
        impl = AddressStore(db)
        address_id = 2

        row_count = asyncio.Future()
        row_count.set_result(1)

        when(db).update("delete from address where address_id = %s", address_id).thenReturn(row_count)

        result = await impl.delete_address_by_id(address_id)

        assert result == 1

    @patch('app.util.database.Db')
    @pytest.mark.asyncio
    async def test_get_address_by_id(self, db: Db):
        impl = AddressStore(db)
        address_id = 2

        address_dto_result = asyncio.Future()
        address_dto_result.set_result(None)

        when(db).query_one("select * from address where address_id = %s", address_dto_from_dict, address_id).thenReturn(address_dto_result)

        result = await impl.get_address_by_id(address_id)

        assert result is None
