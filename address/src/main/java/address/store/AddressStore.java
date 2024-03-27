package address.store;

import dao.jooq.tables.daos.AddressDao;
import dao.jooq.tables.pojos.Address;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.List;

public class AddressStore {

    private static Logger logger = LoggerFactory.getLogger(AddressStore.class);

    private AddressDao addressDao;
    public AddressStore(AddressDao addressDao){
        this.addressDao = addressDao;
    }

    public List<Address> findAll(){
        logger.debug("Started AddressStore.findAll");
        List<Address> result = this.addressDao.findAll();
        logger.debug("Finished AddressStore.findAll");
        return result;
    }


}
