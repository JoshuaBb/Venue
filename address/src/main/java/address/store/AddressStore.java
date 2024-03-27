package address.store;

import dao.jooq.tables.daos.AddressDao;
import dao.jooq.tables.pojos.Address;

import java.util.List;

public class AddressStore {

    private AddressDao addressDao;
    public AddressStore(AddressDao addressDao){
        this.addressDao = addressDao;
        this.addressDao.findAll();
    }

    public List<Address> findAll(){
        return this.addressDao.findAll();
    }


}
