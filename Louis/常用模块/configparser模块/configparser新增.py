__author__ = 'Louis-Pan'

import configparser

config = configparser.ConfigParser()

# 写入节点
config["mysqld"] = {
"character-set-server":"utf8",
"collation-server":"utf8_general_ci",
"performance_schema_max_table_instances":"400",
"table_definition_cache":"400",
"table_open_cache":"256"
}

# 写入节点
config["mysqld_safe"] = {}
config["mysqld_safe"]["log-error"] = "/var/log/mysqld.log"
config["mysqld_safe"]["pid-file"] = "/var/run/mysqld/mysqld.pid"

# 生成文件
with open("mysql.ini",'w') as f:
    config.write(f)