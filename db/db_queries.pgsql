SELECT * FROM child;
SELECT * FROM parent;

INSERT INTO parent (email, first_name, last_name, hashed_password, is_active, is_superuser) 
 	VALUES ('parent1@rak.com', 'parent1_first_name', 'parent1_last_name', '1234', true, true);
	
INSERT INTO parent (email, first_name, last_name, hashed_password, is_active, is_superuser) 
	VALUES ('parent2@rak.com', 'parent2_first_name', 'parent2_last_name', '1234', true, true);
	
INSERT INTO parent (email, first_name, last_name, hashed_password, is_active, is_superuser) 
	VALUES ('parent3@rak.com', 'parent3_first_name', 'parent3_last_name', '1234', true, true)
	
	
-- Children
INSERT INTO child (parent_id, child_name, "date") 
	VALUES (1, 'parent1_child1', CURRENT_TIMESTAMP);
INSERT INTO child (parent_id, child_name, "date") 
	VALUES (1, 'parent1_child2', CURRENT_TIMESTAMP);
INSERT INTO child (parent_id, child_name, "date") 
	VALUES (1, 'parent1_child3', CURRENT_TIMESTAMP);
	
INSERT INTO child (parent_id, child_name, "date") 
	VALUES (2, 'parent2_child1', CURRENT_TIMESTAMP);
INSERT INTO child (parent_id, child_name, "date") 
	VALUES (2, 'parent2_child2', CURRENT_TIMESTAMP);
	
INSERT INTO child (parent_id, child_name, "date") 
	VALUES (3, 'parent3_child1', CURRENT_TIMESTAMP)	