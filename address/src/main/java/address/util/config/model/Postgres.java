package address.util.config.model;

public class Postgres {
    private String host;

    private String user;
    private int port;
    private String database;
    private String password;

    public Postgres(){}

    public Postgres(String user, int port, String host, String database, String password) {
        this.user = user;
        this.port = port;
        this.database = database;
        this.password = password;
        this.host = host;
    }

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }
}
