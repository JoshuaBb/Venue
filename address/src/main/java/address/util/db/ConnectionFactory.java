package address.util.db;

import address.util.config.model.Database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectionFactory {

    private Database database;

    public ConnectionFactory(Database database) {
        this.database = database;
    }

    public Connection initialize() throws SQLException {
        return DriverManager.getConnection(database.getUrl(), database.getUser(), database.getPassword());
    }
}
