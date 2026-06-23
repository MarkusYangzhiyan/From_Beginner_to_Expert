-- beginner_to_expert.agent_memory 定义

CREATE TABLE `agent_memory` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_modify_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `branch_id` varchar(64) NOT NULL,
  `industry` varchar(100) NOT NULL,
  `review_point_name` varchar(255) NOT NULL,
  `review_point` text NOT NULL,
  `risk_name` varchar(255) DEFAULT NULL,
  `risk_type` varchar(100) DEFAULT NULL,
  `memory_graph` json DEFAULT NULL,
  `memory_text` longtext,
  PRIMARY KEY (`id`),
  KEY `idx_scope_review_name` (`branch_id`,`industry`,`review_point_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;