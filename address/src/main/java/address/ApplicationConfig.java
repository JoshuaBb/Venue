package address;

import address.util.config.model.Grpc;
import address.util.config.model.Postgres;

public class ApplicationConfig {
    private Grpc grpc;
    private Postgres postgres;

    public ApplicationConfig(){}

    public ApplicationConfig(Grpc grpc, Postgres postgres) {
        this.grpc = grpc;
        this.postgres = postgres;
    }

    public Grpc getGrpc() {
        return grpc;
    }

    public void setGrpc(Grpc grpc) {
        this.grpc = grpc;
    }

    public Postgres getPostgres() {
        return postgres;
    }

    public void setPostgres(Postgres postgres) {
        this.postgres = postgres;
    }
}
