package address.util.config.model;

public class Grpc {
    private int port;

    public Grpc(){}

    public Grpc(int port) {
        this.port = port;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
}
