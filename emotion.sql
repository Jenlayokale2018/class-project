SELECT * FROM face_emotions;
CREATE TABLE IF NOT EXISTS face_emotions (
  `id` int(11) NOT NULL auto_increment,   
  `face_id` varchar(50) NOT NULL,       
  `emotion` varchar(256)  NOT NULL, 
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,    
   PRIMARY KEY  (`id`)
);