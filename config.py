from configparser import ConfigParser

def parse(config_file, section):    
    config_file_path = config_file
    if (len(config_file_path) > 0 and len(section) > 0):
        config_parser = ConfigParser()
        config_parser.read(config_file_path)
        if (config_parser.has_section(section)):
            config_params = config_parser.items(section)
            db_conn_dict = {}
            for config_param in config_params:
                key = config_param[0]
                value = config_param[1]
                db_conn_dict[key] = value

            return db_conn_dict
