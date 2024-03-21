package address;

import address.rpc.HelloWorldServiceImpl;
import address.util.config.model.ConfigFactory;
import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.ServerServiceDefinition;
import io.grpc.protobuf.services.ProtoReflectionService;

import java.io.IOException;
import java.util.Collections;
import java.util.List;

public class MainServer {

    public static void main(String[] args) {
        HelloWorldServiceImpl hello = new HelloWorldServiceImpl();
        ServerServiceDefinition helloService = hello.bindService();
        List<ServerServiceDefinition> services = Collections.singletonList(helloService);

        try {
            ApplicationConfig config = ConfigFactory.intialize(ApplicationConfig.class, Collections.emptyList());
            Server server = ServerBuilder
                    .forPort(config.getGrpc().getPort())
                    .addServices(services)
                    .addService(ProtoReflectionService.newInstance())
                    .build();

            server.start();
            System.out.println("Application started");
            server.awaitTermination();
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }


    }

}