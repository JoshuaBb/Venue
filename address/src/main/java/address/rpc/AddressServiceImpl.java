package address.rpc;

import address.proto.AddressServiceGrpc.AddressServiceImplBase;
import address.proto.GetAddressRequest;
import address.proto.GetAddressResponse;
import io.grpc.stub.StreamObserver;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class AddressServiceImpl extends AddressServiceImplBase {
    Logger logger = LoggerFactory.getLogger(AddressServiceImpl.class);

    @Override
    public void getAddresses(GetAddressRequest request, StreamObserver<GetAddressResponse> responseObserver) {
        logger.debug("Starting GetAddress Request");

        logger.debug("Finishing GetAddresses Request");
    }
}
