package address.controller;

import address.store.AddressStore;

public class AddressController {
    private AddressStore addressStore;

    public AddressController(AddressStore addressStore) {
        this.addressStore = addressStore;
    }


}
