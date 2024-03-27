package address.controller;

import address.proto.GetAddressResponse;
import address.rpc.transformer.AddressTransformer;
import address.store.AddressStore;

public class AddressController {
    private AddressStore addressStore;

    public AddressController(AddressStore addressStore) {
        this.addressStore = addressStore;
    }

    public GetAddressResponse getAddresses(){
        var addresses = this.addressStore.findAll()
                .stream()
                .map(AddressTransformer::toGrpc).toList();
        var builder = GetAddressResponse.newBuilder();
        for(int i = 0; i < addresses.size(); i++){
            builder.setAddresses(i, addresses.get(i));
        }
        return builder.build();
    }


}
