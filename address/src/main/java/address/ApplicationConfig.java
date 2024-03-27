package address;

import address.util.config.model.Grpc;
import address.util.config.model.Database;

public class ApplicationConfig {
    private Grpc grpc;
    private Database database;

    public ApplicationConfig(){}

    public ApplicationConfig(Grpc grpc) {
        this.grpc = grpc;
        this.database = database;
    }

    public Grpc getGrpc() {
        return grpc;
    }

    public void setGrpc(Grpc grpc) {
        this.grpc = grpc;
    }

    public Database getDatabase() {
        return database;
    }

    public void setDatabase(Database database) {
        this.database = database;
    }
}
