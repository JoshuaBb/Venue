package address.rpc;

import address.proto.HelloWorldRequest;
import address.proto.HelloWorldResponse;
import address.proto.HelloWorldServiceGrpc.HelloWorldServiceImplBase;
import io.grpc.stub.StreamObserver;


/**
 * Test service for GRPC implementation. Streaming is cool
 */
public class HelloWorldServiceImpl extends HelloWorldServiceImplBase  {
    @Override
    public StreamObserver<HelloWorldRequest> sayHello(StreamObserver<HelloWorldResponse> responseObserver) {
        return new StreamObserver<>() {
            @Override
            public void onNext(HelloWorldRequest value) {
                HelloWorldResponse response = HelloWorldResponse.newBuilder().setGreeting("hello " + value.getName()).build();
                responseObserver.onNext(response);
            }

            @Override
            public void onError(Throwable t) {
                responseObserver.onError(t);
            }

            @Override
            public void onCompleted() {
                responseObserver.onCompleted();
            }
        };
    }
}
