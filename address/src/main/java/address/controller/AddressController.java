package address.controller;

import address.proto.Address;
import address.proto.GetAddressResponse;
import address.rpc.transformer.AddressTransformer;
import address.store.AddressStore;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


import java.util.List;

public class AddressController {

    private static Logger logger = LoggerFactory.getLogger(AddressController.class);

    private AddressStore addressStore;

    public AddressController(AddressStore addressStore) {
        this.addressStore = addressStore;
    }

    public GetAddressResponse getAddresses(){
        logger.debug("Fetching all addresses");
        List<Address> addresses = this.addressStore.findAll()
                .stream()
                .map(AddressTransformer::toGrpc)
                .toList();
        logger.debug("Finished fetching all addresses");

        var builder = GetAddressResponse.newBuilder();

        for(int i = 0; i < addresses.size(); i++){
            builder.setAddresses(i, addresses.get(i));
        }
        return builder.build();
    }


}
