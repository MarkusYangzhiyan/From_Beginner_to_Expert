CREATE USER IF NOT EXISTS 'app_user'@'%' IDENTIFIED BY 'AppUser2026';
CREATE USER IF NOT EXISTS 'readonly_user'@'%' IDENTIFIED BY 'ReadOnly2026';

ALTER USER 'app_user'@'%' IDENTIFIED BY 'AppUser2026';
ALTER USER 'readonly_user'@'%' IDENTIFIED BY 'ReadOnly2026';

REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'app_user'@'%';
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'readonly_user'@'%';

GRANT SELECT, INSERT, UPDATE, DELETE
ON products.*
TO 'app_user'@'%';

GRANT SELECT
ON products.*
TO 'readonly_user'@'%';

SHOW GRANTS FOR 'app_user'@'%';
SHOW GRANTS FOR 'readonly_user'@'%';