package address.util.config.model;

import com.fasterxml.jackson.databind.Module;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;

import java.io.File;
import java.io.IOException;
import java.util.List;

public class ConfigFactory{
    public static <Config> Config intialize(Class<Config> classValue, List<Module> modules) throws IOException {
        ObjectMapper mapper = new ObjectMapper(new YAMLFactory());
        mapper.findAndRegisterModules();
        mapper.registerModules(modules);
        Config application = mapper.readValue(new File("src/main/resources/application.conf"),classValue);
        return application;
    }
}
