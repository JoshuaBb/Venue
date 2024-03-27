package address;

import address.controller.AddressController;
import address.rpc.AddressServiceImpl;
import address.rpc.HelloWorldServiceImpl;
import address.store.AddressStore;
import address.util.config.model.ConfigFactory;
import address.util.db.ConnectionFactory;
import dao.jooq.tables.daos.AddressDao;
import io.grpc.BindableService;
import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.protobuf.services.ProtoReflectionService;
import org.jooq.Configuration;
import org.jooq.SQLDialect;
import org.jooq.impl.DefaultConfiguration;

import java.io.IOException;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.Collections;
import java.util.stream.Stream;

public class MainServer {

    public static void main(String[] args) {

        try {
            ApplicationConfig config = ConfigFactory.intialize(ApplicationConfig.class, Collections.emptyList());
            try (Connection connection = new ConnectionFactory(config.getDatabase()).initialize()) {
                // Initializing DAO
                Configuration configuration = new DefaultConfiguration().set(connection).set(SQLDialect.POSTGRES);
                AddressDao addressDao = new AddressDao(configuration);

                // Initializing stores
                AddressStore addressStore = new AddressStore(addressDao);

                // Initializing Controllers
                AddressController addressController = new AddressController(addressStore);

                // Initializing RPC
                HelloWorldServiceImpl hello = new HelloWorldServiceImpl();
                AddressServiceImpl addressService = new AddressServiceImpl(addressController);

                Server server = ServerBuilder
                        .forPort(config.getGrpc().getPort())
                        .addServices(Stream.of(hello, addressService).map(BindableService::bindService).toList())
                        .addService(ProtoReflectionService.newInstance())
                        .build();

                server.start();
                System.out.println("Application started");
                server.awaitTermination();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            } catch (IOException e) {
                throw new RuntimeException(e);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

}