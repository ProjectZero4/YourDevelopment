
    while ! mysqladmin ping -h "yd.database" --silent; do
        sleep 1
    done
    
        mysql -h "yd.database" -u root -pyour_development mysql < "/root/sql/database/your_league.sql"
    
        mysql -h "yd.database" -u root -pyour_development mysql < "/root/sql/database/your_quests.sql"
    

    while ! mysqladmin ping -h "yd.database_1" --silent; do
        sleep 1
    done
    
        mysql -h "yd.database_1" -u root -pyour_development mysql < "/root/sql/database_1/your_status.sql"
    
