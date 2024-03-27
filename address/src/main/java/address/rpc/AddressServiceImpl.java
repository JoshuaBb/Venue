package address.rpc;

import address.controller.AddressController;
import address.proto.AddressServiceGrpc.AddressServiceImplBase;
import address.proto.GetAddressRequest;
import address.proto.GetAddressResponse;
import io.grpc.stub.StreamObserver;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class AddressServiceImpl extends AddressServiceImplBase {
    Logger logger = LoggerFactory.getLogger(AddressServiceImpl.class);

    private AddressController addressController;

    public AddressServiceImpl(AddressController addressController){
        this.addressController= addressController;
    }

    @Override
    public void getAddresses(GetAddressRequest request, StreamObserver<GetAddressResponse> responseObserver) {
        logger.debug("Starting GetAddress Request");
        responseObserver.onNext(this.addressController.getAddresses());
        responseObserver.onCompleted();
        logger.debug("Finishing GetAddresses Request");
    }
}
