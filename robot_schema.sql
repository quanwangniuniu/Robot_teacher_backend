/*
 Navicat Premium Data Transfer

 Source Server         : ssmd67h124v
 Source Server Type    : MySQL
 Source Server Version : 50744
 Source Host           : localhost:3306
 Source Schema         : robot_schema

 Target Server Type    : MySQL
 Target Server Version : 50744
 File Encoding         : 65001

 Date: 05/04/2024 21:08:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for administratorhandler_adminuser
-- ----------------------------
DROP TABLE IF EXISTS `administratorhandler_adminuser`;
CREATE TABLE `administratorhandler_adminuser`  (
  `admin_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `phone_number` varchar(15) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(254) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `password` varchar(128) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`admin_id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `phone_number`(`phone_number`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of administratorhandler_adminuser
-- ----------------------------
INSERT INTO `administratorhandler_adminuser` VALUES (1, 'lihong', '11023928122', '12312@qq.com', 1, '1111');

-- ----------------------------
-- Table structure for administratorhandler_meicymodel
-- ----------------------------
DROP TABLE IF EXISTS `administratorhandler_meicymodel`;
CREATE TABLE `administratorhandler_meicymodel`  (
  `model_id` int(11) NOT NULL AUTO_INCREMENT,
  `learningRate` double NOT NULL,
  `batchSize` int(11) NOT NULL,
  `epoches` int(11) NOT NULL,
  `hiddenLayerSize` int(11) NOT NULL,
  `vocabularySize` bigint(20) NOT NULL,
  `maxSeqLength` int(11) NOT NULL,
  `dropoutRate` double NOT NULL,
  `gradientClippingThreshold` double NOT NULL,
  `optimizer` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `lossFunction` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`model_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of administratorhandler_meicymodel
-- ----------------------------
INSERT INTO `administratorhandler_meicymodel` VALUES (1, 0.543, 256, 40, 512, 100000, 500, 0.141, 1.511, 'sgd', 'binaryCrossEntropy');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 61 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add student user', 7, 'add_studentuser');
INSERT INTO `auth_permission` VALUES (26, 'Can change student user', 7, 'change_studentuser');
INSERT INTO `auth_permission` VALUES (27, 'Can delete student user', 7, 'delete_studentuser');
INSERT INTO `auth_permission` VALUES (28, 'Can view student user', 7, 'view_studentuser');
INSERT INTO `auth_permission` VALUES (29, 'Can add teacher user', 8, 'add_teacheruser');
INSERT INTO `auth_permission` VALUES (30, 'Can change teacher user', 8, 'change_teacheruser');
INSERT INTO `auth_permission` VALUES (31, 'Can delete teacher user', 8, 'delete_teacheruser');
INSERT INTO `auth_permission` VALUES (32, 'Can view teacher user', 8, 'view_teacheruser');
INSERT INTO `auth_permission` VALUES (33, 'Can add admin user', 9, 'add_adminuser');
INSERT INTO `auth_permission` VALUES (34, 'Can change admin user', 9, 'change_adminuser');
INSERT INTO `auth_permission` VALUES (35, 'Can delete admin user', 9, 'delete_adminuser');
INSERT INTO `auth_permission` VALUES (36, 'Can view admin user', 9, 'view_adminuser');
INSERT INTO `auth_permission` VALUES (37, 'Can add robot class room', 10, 'add_robotclassroom');
INSERT INTO `auth_permission` VALUES (38, 'Can change robot class room', 10, 'change_robotclassroom');
INSERT INTO `auth_permission` VALUES (39, 'Can delete robot class room', 10, 'delete_robotclassroom');
INSERT INTO `auth_permission` VALUES (40, 'Can view robot class room', 10, 'view_robotclassroom');
INSERT INTO `auth_permission` VALUES (41, 'Can add conversation', 11, 'add_conversation');
INSERT INTO `auth_permission` VALUES (42, 'Can change conversation', 11, 'change_conversation');
INSERT INTO `auth_permission` VALUES (43, 'Can delete conversation', 11, 'delete_conversation');
INSERT INTO `auth_permission` VALUES (44, 'Can view conversation', 11, 'view_conversation');
INSERT INTO `auth_permission` VALUES (45, 'Can add message', 12, 'add_message');
INSERT INTO `auth_permission` VALUES (46, 'Can change message', 12, 'change_message');
INSERT INTO `auth_permission` VALUES (47, 'Can delete message', 12, 'delete_message');
INSERT INTO `auth_permission` VALUES (48, 'Can view message', 12, 'view_message');
INSERT INTO `auth_permission` VALUES (49, 'Can add chart image', 13, 'add_chartimage');
INSERT INTO `auth_permission` VALUES (50, 'Can change chart image', 13, 'change_chartimage');
INSERT INTO `auth_permission` VALUES (51, 'Can delete chart image', 13, 'delete_chartimage');
INSERT INTO `auth_permission` VALUES (52, 'Can view chart image', 13, 'view_chartimage');
INSERT INTO `auth_permission` VALUES (53, 'Can add class room message', 14, 'add_classroommessage');
INSERT INTO `auth_permission` VALUES (54, 'Can change class room message', 14, 'change_classroommessage');
INSERT INTO `auth_permission` VALUES (55, 'Can delete class room message', 14, 'delete_classroommessage');
INSERT INTO `auth_permission` VALUES (56, 'Can view class room message', 14, 'view_classroommessage');
INSERT INTO `auth_permission` VALUES (57, 'Can add meicy model', 15, 'add_meicymodel');
INSERT INTO `auth_permission` VALUES (58, 'Can change meicy model', 15, 'change_meicymodel');
INSERT INTO `auth_permission` VALUES (59, 'Can delete meicy model', 15, 'delete_meicymodel');
INSERT INTO `auth_permission` VALUES (60, 'Can view meicy model', 15, 'view_meicymodel');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(254) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for classroomhandler_classroommessage
-- ----------------------------
DROP TABLE IF EXISTS `classroomhandler_classroommessage`;
CREATE TABLE `classroomhandler_classroommessage`  (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `class_id` int(11) NOT NULL,
  `message_content` varchar(2000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_type` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `message_avatar` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `user_name` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`message_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classroomhandler_classroommessage
-- ----------------------------
INSERT INTO `classroomhandler_classroommessage` VALUES (1, 1, '这是我在群里发的第一条消息', 'teacher', 'https://robohash.org/duck', 'lixiaobin');
INSERT INTO `classroomhandler_classroommessage` VALUES (4, 1, '今天软件工程还有什么问题么，请同学给我私信', 'teacher', 'https://robohash.org/duck', 'lixiaobin');
INSERT INTO `classroomhandler_classroommessage` VALUES (5, 1, '没有同学说话就默认大家都没问题了！', 'teacher', 'https://robohash.org/duck', 'lixiaobin');
INSERT INTO `classroomhandler_classroommessage` VALUES (6, 1, '我是老师，我就不能有问题么？', 'teacher', 'https://robohash.org/duck', 'kaihongmei');
INSERT INTO `classroomhandler_classroommessage` VALUES (7, 1, '我感觉软件工程的UML建模部分还是有些不理解的地方', 'student', 'https://robohash.org/duck', 'liguorui');
INSERT INTO `classroomhandler_classroommessage` VALUES (8, 1, '今天哪个同学有时间流一下？', 'teacher', 'https://api.dicebear.com/7.x/miniavs/svg?seed=46', 'lixiaobin');
INSERT INTO `classroomhandler_classroommessage` VALUES (9, 1, '我有空！', 'student', 'https://api.dicebear.com/7.x/miniavs/svg?seed=70', 'liguorui');

-- ----------------------------
-- Table structure for classroomhandler_robotclassroom
-- ----------------------------
DROP TABLE IF EXISTS `classroomhandler_robotclassroom`;
CREATE TABLE `classroomhandler_robotclassroom`  (
  `class_id` int(11) NOT NULL AUTO_INCREMENT,
  `class_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `class_avatar` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`class_id`) USING BTREE,
  UNIQUE INDEX `classroomhandler_robotclassroom_class_name_3fbac5c4_uniq`(`class_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classroomhandler_robotclassroom
-- ----------------------------
INSERT INTO `classroomhandler_robotclassroom` VALUES (1, '20智72', 'https://robohash.org/lion');
INSERT INTO `classroomhandler_robotclassroom` VALUES (2, '20智71', 'https://robohash.org/duck');
INSERT INTO `classroomhandler_robotclassroom` VALUES (3, '21商131', 'https://robohash.org/lion');
INSERT INTO `classroomhandler_robotclassroom` VALUES (4, '21智72', 'https://robohash.org/dog');
INSERT INTO `classroomhandler_robotclassroom` VALUES (5, '21智71', 'https://robohash.org/lion');
INSERT INTO `classroomhandler_robotclassroom` VALUES (6, '22智71', 'https://robohash.org/monkey');
INSERT INTO `classroomhandler_robotclassroom` VALUES (7, '23智81', 'https://robohash.org/duck');
INSERT INTO `classroomhandler_robotclassroom` VALUES (8, '20智52', 'https://robohash.org/dog');
INSERT INTO `classroomhandler_robotclassroom` VALUES (9, '21智52', 'https://robohash.org/monkey');
INSERT INTO `classroomhandler_robotclassroom` VALUES (10, '20智70', 'https://robohash.org/monkey');
INSERT INTO `classroomhandler_robotclassroom` VALUES (13, '24智72', 'https://robohash.org/banana');
INSERT INTO `classroomhandler_robotclassroom` VALUES (15, '19智71', 'https://robohash.org/monkey');
INSERT INTO `classroomhandler_robotclassroom` VALUES (16, '21商144', 'https://robohash.org/pandas');
INSERT INTO `classroomhandler_robotclassroom` VALUES (17, '20智78', 'https://robohash.org/lion');
INSERT INTO `classroomhandler_robotclassroom` VALUES (18, '18智71', 'https://robohash.org/tree');

-- ----------------------------
-- Table structure for classroomhandler_robotclassroom_student
-- ----------------------------
DROP TABLE IF EXISTS `classroomhandler_robotclassroom_student`;
CREATE TABLE `classroomhandler_robotclassroom_student`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `robotclassroom_id` int(11) NOT NULL,
  `studentuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `classroomhandler_robotcl_robotclassroom_id_studen_44806606_uniq`(`robotclassroom_id`, `studentuser_id`) USING BTREE,
  INDEX `classroomhandler_rob_studentuser_id_1ccfb9d9_fk_studentha`(`studentuser_id`) USING BTREE,
  CONSTRAINT `classroomhandler_rob_robotclassroom_id_2f6036eb_fk_classroom` FOREIGN KEY (`robotclassroom_id`) REFERENCES `classroomhandler_robotclassroom` (`class_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `classroomhandler_rob_studentuser_id_1ccfb9d9_fk_studentha` FOREIGN KEY (`studentuser_id`) REFERENCES `studenthandler_studentuser` (`student_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classroomhandler_robotclassroom_student
-- ----------------------------
INSERT INTO `classroomhandler_robotclassroom_student` VALUES (2, 1, 1);
INSERT INTO `classroomhandler_robotclassroom_student` VALUES (1, 2, 1);
INSERT INTO `classroomhandler_robotclassroom_student` VALUES (3, 8, 1);
INSERT INTO `classroomhandler_robotclassroom_student` VALUES (6, 13, 1);
INSERT INTO `classroomhandler_robotclassroom_student` VALUES (4, 15, 1);

-- ----------------------------
-- Table structure for classroomhandler_robotclassroom_teacher
-- ----------------------------
DROP TABLE IF EXISTS `classroomhandler_robotclassroom_teacher`;
CREATE TABLE `classroomhandler_robotclassroom_teacher`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `robotclassroom_id` int(11) NOT NULL,
  `teacheruser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `classroomhandler_robotcl_robotclassroom_id_teache_7e24aa3d_uniq`(`robotclassroom_id`, `teacheruser_id`) USING BTREE,
  INDEX `classroomhandler_rob_teacheruser_id_6b389272_fk_teacherha`(`teacheruser_id`) USING BTREE,
  CONSTRAINT `classroomhandler_rob_robotclassroom_id_94cfe0b4_fk_classroom` FOREIGN KEY (`robotclassroom_id`) REFERENCES `classroomhandler_robotclassroom` (`class_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `classroomhandler_rob_teacheruser_id_6b389272_fk_teacherha` FOREIGN KEY (`teacheruser_id`) REFERENCES `teacherhandler_teacheruser` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classroomhandler_robotclassroom_teacher
-- ----------------------------
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (1, 1, 1);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (12, 1, 2);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (2, 2, 1);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (13, 2, 2);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (3, 3, 1);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (4, 4, 1);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (5, 5, 1);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (6, 6, 1);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (7, 8, 1);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (8, 9, 1);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (14, 10, 2);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (9, 10, 3);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (10, 13, 3);
INSERT INTO `classroomhandler_robotclassroom_teacher` VALUES (11, 15, 3);

-- ----------------------------
-- Table structure for conversationhandler_conversation
-- ----------------------------
DROP TABLE IF EXISTS `conversationhandler_conversation`;
CREATE TABLE `conversationhandler_conversation`  (
  `conversation_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `start_time` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `end_time` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `title` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `user_type` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `robot_model` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `robot_prompt` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `roles` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `rate` double NOT NULL,
  PRIMARY KEY (`conversation_id`) USING BTREE,
  UNIQUE INDEX `conversationhandler_conversation_title_2ccd34e9_uniq`(`title`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of conversationhandler_conversation
-- ----------------------------
INSERT INTO `conversationhandler_conversation` VALUES (1, 1, '2024-01-31 14:54:38', '2024-01-31 14:02:29', '代码机器人', 1, 'student', 'qwen-max', 'dfsf', '哈哈代码工程师', 3);
INSERT INTO `conversationhandler_conversation` VALUES (4, 1, '2024-01-31 15:03:48', '2024-01-31 14:25:55', '专业课程机器人', 1, 'student', 'qwen-max', '你是一个代码工程师，需要讲进行毕业设计的代码思路提醒和作用', '设计助手', 3);
INSERT INTO `conversationhandler_conversation` VALUES (5, 1, '2024-01-31 15:11:35', '2024-01-31 14:25:55', '计算机设计机器人', 1, 'student', 'qwen-max', '你是一个代码工程师，需要讲进行毕业设计的代码思路提醒和作用', '专业课程助手', 0);
INSERT INTO `conversationhandler_conversation` VALUES (6, 1, '2024-02-01 15:09:03', '2024-02-01 15:09:13', '软件工程小助手', 1, 'student', 'qwen-max', '解答软件工程方面的问题', '设计助手', 5);
INSERT INTO `conversationhandler_conversation` VALUES (7, 1, '2024-02-01 15:27:09', '2024-02-01 15:27:14', '软件测试机器人试用', 1, 'student', 'qwen-max', '你需要告诉我软件测试的名词概念解析和概念分析', '概念解释助手', 0);
INSERT INTO `conversationhandler_conversation` VALUES (8, 2, '2024-02-18 08:47:28', '2024-02-29 08:51:58', '数据库设计机器人', 1, 'student', 'qwen-max', '对数据库进行详细的设计', '设计助手', 0);
INSERT INTO `conversationhandler_conversation` VALUES (9, 2, '2024-02-18 08:52:44', '2025-03-07 08:52:43', 'UML建模机器人', 1, 'student', 'qwen-max', '解答UML建模相关的问题', '专业课程助手', 0);
INSERT INTO `conversationhandler_conversation` VALUES (10, 2, '2024-02-18 08:54:42', '2025-03-27 08:54:41', '程序设计机器人', 1, 'student', 'qwen-max', '编写详细且可读性强的代码', '代码工程师', 0);
INSERT INTO `conversationhandler_conversation` VALUES (11, 1, '2024-02-18 09:09:07', '2025-02-07 09:08:48', '计算机网络老师', 1, 'student', 'qwen-max', '进行计算机网络题目的辅导', '设计助手', 2);
INSERT INTO `conversationhandler_conversation` VALUES (12, 1, '2024-03-02 09:08:58', '2024-03-08 09:01:26', 'DevOps辅导员', 1, 'teacher', 'qwen-max', '当一名安静的DevOps辅导员，我问你啥问题你回答即可不要多嘴', 'DevOps工程师', 0.5);
INSERT INTO `conversationhandler_conversation` VALUES (13, 2, '2024-03-11 17:55:33', '2026-03-26 17:55:32', '开老师的辅助机器人', 1, 'teacher', 'qwen-max', '你是一个懂得操作系统的机器人，你需要进行概念解释', '概念解释助手', 3.5);

-- ----------------------------
-- Table structure for conversationhandler_message
-- ----------------------------
DROP TABLE IF EXISTS `conversationhandler_message`;
CREATE TABLE `conversationhandler_message`  (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `conversation_id` int(11) NOT NULL,
  `message_content` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `message_type` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`message_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 34 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of conversationhandler_message
-- ----------------------------
INSERT INTO `conversationhandler_message` VALUES (1, 4, '你好', 'right');
INSERT INTO `conversationhandler_message` VALUES (2, 4, '你好！作为一名代码工程师，我专注于编写高质量、高效率的代码，并致力于解决各类软件开发和编程问题。如果你有任何关于编程语言、算法、数据结构、项目开发或技术选型等方面的问题，欢迎随时向我咨询。让我们一起探索编程世界的无限可能！', 'left');
INSERT INTO `conversationhandler_message` VALUES (4, 7, '你好！有什么我能为你解释的概念或问题吗？', 'left');
INSERT INTO `conversationhandler_message` VALUES (5, 6, '软件工程', 'right');
INSERT INTO `conversationhandler_message` VALUES (6, 6, '软件工程是一门系统性的学科，它将工程化的原则、方法和实践应用于软件开发、维护和管理过程中，旨在构建高质量、可维护、高效率的软件产品。在软件工程中，涵盖了需求分析、设计、编码、测试、维护等多个阶段，并强调团队协作、项目管理和质量控制等要素。其目标是通过合理的组织与计划，运用现代科学技术知识，经济地开发出满足用户需求、达到预期功能性能指标并且按时交付的软件系统。同时，软件工程还注重软件开发过程中的文档编写和标准化，以及对新的开发技术、工具和框架的研究与应用。', 'left');
INSERT INTO `conversationhandler_message` VALUES (7, 6, '你好', 'right');
INSERT INTO `conversationhandler_message` VALUES (9, 7, '你好', 'right');
INSERT INTO `conversationhandler_message` VALUES (10, 7, '你好！有什么问题我可以帮助你解答吗？', 'left');
INSERT INTO `conversationhandler_message` VALUES (11, 7, '你可以干嘛', 'right');
INSERT INTO `conversationhandler_message` VALUES (12, 7, '作为AI助手，我可以帮助您完成多项任务，包括但不限于：\n\n1. 知识问答：解答您在各个领域的疑问，提供详尽的知识解析。\n\n2. 智能推荐：根据您的需求，推荐适合的商品、电影、书籍等资源。\n\n3. 学习辅导：协助学习各类知识，如语言学习、专业课程咨询等。\n\n4. 新闻资讯获取：为您提供最新的新闻热点和实时资讯。\n\n5. 生活服务：如天气查询、菜谱推荐、健康管理等生活实用信息的提供。\n\n6. 创意生成：帮助用户进行头脑风暴，提供创新观点或创意写作素材。\n\n7. 聊天交流：与用户进行日常对话交流，提供情感支持陪伴。\n\n8. 企业应用：在商业场景中，可以用于智能客服、数据分析、报告生成等工作。\n\n总的来说，我的目标是通过高效的信息处理能力，为用户提供全面、精准、个性化的服务。', 'left');
INSERT INTO `conversationhandler_message` VALUES (13, 7, '你是什么角色！', 'right');
INSERT INTO `conversationhandler_message` VALUES (14, 7, '我是阿里云研发的超大规模语言模型，我叫通义千问，主要功能是生成各种类型的文本，如文章、故事、诗歌、故事等，并能够根据不同的场景和需求进行变换和扩展。同时，我还能够回答各种问题，提供详尽而准确的信息，帮助用户解决问题、获取知识以及进行创作灵感激发。在与用户的交互中，我可以扮演多种角色，如智能助手、信息检索专家、内容创作者、对话伙伴等。', 'left');
INSERT INTO `conversationhandler_message` VALUES (15, 7, '我给你的什么角色？', 'right');
INSERT INTO `conversationhandler_message` VALUES (16, 7, '作为AI语言模型，我并没有具体的“角色”由您赋予。我是阿里云研发的超大规模语言模型，主要功能是为用户提供信息查询、问题解答、内容生成、对话交互等各类自然语言处理任务的服务。您可以将我视为一个无所不知的知识库助手、贴心的聊天伙伴或高效的文本处理工具，根据您的需求来与我进行互动。', 'left');
INSERT INTO `conversationhandler_message` VALUES (17, 7, '写一个斐波那契数列递归程序', 'right');
INSERT INTO `conversationhandler_message` VALUES (18, 7, '当然可以，以下是一个使用Python编写的斐波那契数列递归程序：\n\n```python\ndef fibonacci(n):\n    # 斐波那契数列的递归定义\n    # F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) (n >= 2)\n    \n    if n <= 0:\n        return \"输入值应大于0\"\n    elif n == 1:\n        return 0\n    elif n == 2:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n\n# 测试程序\nfor i in range(10):\n    print(fibonacci(i))\n```\n\n这段程序会计算并打印斐波那契数列的前10项。注意，由于递归实现的效率较低（存在大量重复计算），对于较大的n值，建议采用动态规划等更高效的方法来求解斐波那契数列。', 'left');
INSERT INTO `conversationhandler_message` VALUES (19, 7, '软件测试是什么', 'right');
INSERT INTO `conversationhandler_message` VALUES (20, 7, '软件测试是一种系统性的质量控制过程，主要目的是验证和确认软件产品的功能、性能、兼容性、安全性、可靠性等是否满足既定的需求规格和用户期望。在软件开发过程中，测试人员通过设计和执行测试用例，发现并记录软件中的错误（Bug）、缺陷或不足之处，并反馈给开发团队进行修正，以确保最终交付的软件产品具有较高的质量和可用性。\n\n具体来说，软件测试涵盖了单元测试、集成测试、系统测试、验收测试等多个阶段，同时也会涉及回归测试、压力测试、性能测试、兼容性测试等多种类型，确保软件在不同环境和条件下都能稳定可靠地运行。', 'left');
INSERT INTO `conversationhandler_message` VALUES (21, 7, '银渐层是什么', 'right');
INSERT INTO `conversationhandler_message` VALUES (22, 7, '“银渐层”是指一种猫的毛色花色类型，主要出现在英国短毛猫（British Shorthair）品种中，也有部分其他品种如布偶猫等存在这种毛色。银渐层猫的毛色特征是底层绒毛为白色，而毛尖则呈现灰色，整体看起来像是银色，并且颜色深浅有层次过渡，因此得名“银渐层”。其眼睛多为绿色或蓝绿，品相甜美可爱，深受爱猫人士喜爱。', 'left');
INSERT INTO `conversationhandler_message` VALUES (23, 1, '您好', 'right');
INSERT INTO `conversationhandler_message` VALUES (24, 1, '您好！有什么我能为您做的吗？作为代码工程师，我可以帮助解答您关于编程、软件开发、算法设计等相关问题。如果您有任何需求或疑问，请随时向我提问。', 'left');
INSERT INTO `conversationhandler_message` VALUES (25, 1, '图论的复杂的代码你会写么，写一个我看看？', 'right');
INSERT INTO `conversationhandler_message` VALUES (26, 1, '当然可以，这里我将提供一个简单的图论问题的Python代码实现：寻找无向图中两个节点之间的最短路径，采用Dijkstra算法。\n\n```python\nimport heapq\n\nclass Graph:\n    def __init__(self):\n        self.graph = {}\n\n    def add_edge(self, node1, node2, weight):\n        if node1 not in self.graph:\n            self.graph[node1] = {node2: weight}\n        else:\n            self.graph[node1][node2] = weight\n        # 由于是无向图，所以还要添加反向边\n        if node2 not in self.graph:\n            self.graph[node2] = {node1: weight}\n        else:\n            self.graph[node2][node1] = weight\n\n    def dijkstra(self, start_node, end_node):\n        distances = {node: float(\'infinity\') for node in self.graph}\n        distances[start_node] = 0\n        pq = [(0, start_node)]\n\n        while pq:\n            curr_dist, curr_node = heapq.heappop(pq)\n\n            if distances[curr_node] < curr_dist:\n                continue\n\n            for neighbor, weight in self.graph[curr_node].items():\n                distance = curr_dist + weight\n\n                if distance < distances[neighbor]:\n                    distances[neighbor] = distance\n                    heapq.heappush(pq, (distance, neighbor))\n\n        return distances[end_node]\n\n# 使用示例：\ng = Graph()\ng.add_edge(0, 1, 4)\ng.add_edge(0, 7, 8)\ng.add_edge(1, 7, 11)\ng.add_edge(1, 2, 8)\n# ... 添加其他边...\nprint(g.dijkstra(0, 7))  # 输出节点0到节点7的最短距离\n```\n\n请注意，上述代码是一个简化版的Dijkstra算法实现，并未处理不存在终点或起点不在图中的情况。在实际复杂项目中，可能还需要增加错误处理和优化部分代码结构。', 'left');
INSERT INTO `conversationhandler_message` VALUES (27, 8, '希望创建一个《教学辅助聊天机器人》的数据库，应该如何设计？', 'right');
INSERT INTO `conversationhandler_message` VALUES (28, 8, '设计一个《教学辅助聊天机器人》的数据库需要考虑以下几个核心部分：\n\n1. **知识库**：存储各类学科知识点，包括但不限于课程大纲、概念解释、公式定理、例题解析、实验步骤等。每个知识点应具有唯一标识符，并且可以按照学科、章节、主题进行分类和关联。\n\n   - 知识点表\n     - 知识点ID\n     - 学科类别\n     - 章节编号\n     - 主题\n     - 内容详情（文本或富媒体）\n     - 相关知识点链接\n\n2. **问题-答案对**：构建Q&A对数据库，涵盖学生可能提出的问题及其对应的详尽解答，以便机器人能准确匹配并回复用户。\n\n   - 问题与答案表\n     - 问题ID\n     - 问题内容\n     - 答案内容\n     - 关联知识点ID\n\n3. **用户信息**：记录用户的个人信息、学习进度、偏好等，以便个性化推荐和跟踪辅导效果。\n\n   - 用户信息表\n     - 用户ID\n     - 姓名\n     - 年龄\n     - 学科\n     - 学习进度\n     - 个人偏好设置\n\n4. **交互历史**：保存聊天记录和用户行为数据，用于后续的机器学习训练和优化服务体验。\n\n   - 交互历史表\n     - 记录ID\n     - 用户ID\n     - 交互时间\n     - 交互内容\n     - 机器人响应\n     - 用户反馈\n\n5. **资源库**：如果机器人还提供多媒体教学资源下载或在线观看功能，则需建立资源库，包含视频、音频、文档等信息。\n\n   - 资源库表\n     - 资源ID\n     - 资源名称\n     - 资源类型\n     - 存储路径\n     - 关联知识点ID\n\n在实际设计中，根据具体需求可能还需要添加更多的表结构以支持更复杂的功能，如错题本、测试成绩、答疑解惑记录等。同时，为了保证高效检索和更新，数据库设计时还需充分考虑索引策略以及表之间的关系设计。', 'left');
INSERT INTO `conversationhandler_message` VALUES (29, 10, 'react中props的用法详解', 'right');
INSERT INTO `conversationhandler_message` VALUES (30, 10, '在React中，props（属性）是组件之间传递数据的主要方式。每个React组件都可以接收来自父组件的props，并根据这些props来决定如何渲染自身以及执行哪些行为。\n\n**Props的基本用法：**\n\n1. **定义和接收Props：**\n   在React组件类或函数组件中，通过形参定义props。例如，在一个名为`MyComponent`的函数组件中：\n\n   ```jsx\n   function MyComponent({ name, age }) {\n     return (\n       <div>\n         <h1>Hello, {name}!</h1>\n         <p>You are {age} years old.</p>\n       </div>\n     );\n   }\n   ```\n\n   在这个例子中，`MyComponent`接收两个props：`name`和`age`，并在渲染时使用它们。\n\n2. **父组件传递Props：**\n   父组件可以通过在其标签内添加属性的方式将props传递给子组件：\n\n   ```jsx\n   <MyComponent name=\"Alice\" age={30} />\n   ```\n\n3. **默认Props值：**\n   可以为组件的props设置默认值，以防父组件没有传递对应的props。在函数组件中，可以利用ES6解构赋值结合默认参数实现：\n\n   ```jsx\n   function MyComponent({ name = \'Guest\', age = 0 }) {\n     // ...\n   }\n   ```\n\n4. **类型验证：**\n   使用TypeScript或者prop-types库，可以为props做类型检查，确保组件接收到的数据类型正确。\n\n5. **只读性：**\n   Props在组件内部是只读的，不能直接修改。若需要修改基于props的值，应当使用state并通过事件回调通知父组件更新props。\n\n总结来说，props是React中用于组件间通信的核心机制，它允许我们将数据从父组件流向子组件，保持了数据的单向流动和组件的可复用性。', 'left');
INSERT INTO `conversationhandler_message` VALUES (31, 12, '给现代化计算机教学的方针出一个新方案?', 'right');
INSERT INTO `conversationhandler_message` VALUES (32, 12, '在制定针对现代化计算机教学的新方案时，我们可以结合当前信息技术发展、企业需求以及教育创新趋势，提出以下方针：\n\n1. **课程内容更新与前瞻性**：\n   - 确保课程涵盖最新编程语言和技术框架，如Python、Java、Go、前端React/Vue等，同时引入云计算、大数据、人工智能、区块链、物联网等前沿技术领域知识。\n   \n2. **项目驱动学习**：\n   - 采用实践导向的教学模式，让学生通过解决实际问题或开发真实项目来掌握技能，比如组织编程竞赛、开源项目贡献、实训基地建设等。\n\n3. **跨学科融合**：\n   - 结合计算机科学与其他学科（如数学、物理、艺术设计等）进行交叉融合教学，培养学生利用计算思维解决复杂问题的能力。\n\n4. **软技能培养**：\n   - 强化DevOps理念，教授版本控制、持续集成/持续部署(CI/CD)、容器化和微服务等相关知识，提升学生团队协作和工程化开发能力。\n   \n5. **在线混合式教学**：\n   - 利用现代信息技术搭建线上线下相结合的混合式教学平台，包括MOOCs、SPOCs、虚拟实验室等，实现个性化学习和翻转课堂。\n\n6. **师资队伍建设**：\n   - 加强教师队伍的专业培训，鼓励教师参与业界实践以保持技术敏锐度，并邀请行业专家进行讲座分享，提升教学质量。\n\n7. **创新与创业教育**：\n   - 建立创新创业实践体系，引导学生开展科技创新活动，孵化具有市场潜力的IT项目，培养学生的创业意识和创新能力。\n\n8. **认证体系对接**：\n   - 将国内外知名IT认证考试（如AWS Certified DevOps Engineer、Oracle Certified Professional等）纳入教学计划，帮助学生获得权威资格认证。\n\n9. **国际化视野**：\n   - 开展国际交流项目，引进国外优质教育资源，加强国际合作办学，拓宽学生的全球视野和国际竞争力。\n\n10. **伦理与社会责任教育**：\n    - 注重培养学生遵守数据安全法规、尊重知识产权和关注算法伦理的意识，使学生成为有道德责任感和社会担当的现代计算机专业人才。', 'left');
INSERT INTO `conversationhandler_message` VALUES (33, 1, 'sdfdsfdsf', 'right');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `object_repr` varchar(200) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `model` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (9, 'administratorhandler', 'adminuser');
INSERT INTO `django_content_type` VALUES (15, 'administratorhandler', 'meicymodel');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (13, 'charthandler', 'chartimage');
INSERT INTO `django_content_type` VALUES (14, 'classroomhandler', 'classroommessage');
INSERT INTO `django_content_type` VALUES (10, 'classroomhandler', 'robotclassroom');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (11, 'conversationhandler', 'conversation');
INSERT INTO `django_content_type` VALUES (12, 'conversationhandler', 'message');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (7, 'studenthandler', 'studentuser');
INSERT INTO `django_content_type` VALUES (8, 'teacherhandler', 'teacheruser');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 62 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2024-01-27 02:13:42.839489');
INSERT INTO `django_migrations` VALUES (31, 'auth', '0001_initial', '2024-02-01 08:49:47.203092');
INSERT INTO `django_migrations` VALUES (32, 'admin', '0001_initial', '2024-02-01 08:49:47.205085');
INSERT INTO `django_migrations` VALUES (33, 'admin', '0002_logentry_remove_auto_add', '2024-02-01 08:49:47.206083');
INSERT INTO `django_migrations` VALUES (34, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-01 08:49:47.208074');
INSERT INTO `django_migrations` VALUES (35, 'administratorhandler', '0001_initial', '2024-02-01 08:49:47.209071');
INSERT INTO `django_migrations` VALUES (36, 'contenttypes', '0002_remove_content_type_name', '2024-02-01 08:49:47.211070');
INSERT INTO `django_migrations` VALUES (37, 'auth', '0002_alter_permission_name_max_length', '2024-02-01 08:49:47.212069');
INSERT INTO `django_migrations` VALUES (38, 'auth', '0003_alter_user_email_max_length', '2024-02-01 08:49:47.213060');
INSERT INTO `django_migrations` VALUES (39, 'auth', '0004_alter_user_username_opts', '2024-02-01 08:49:47.214059');
INSERT INTO `django_migrations` VALUES (40, 'auth', '0005_alter_user_last_login_null', '2024-02-01 08:49:47.218070');
INSERT INTO `django_migrations` VALUES (41, 'auth', '0006_require_contenttypes_0002', '2024-02-01 08:49:47.220043');
INSERT INTO `django_migrations` VALUES (42, 'auth', '0007_alter_validators_add_error_messages', '2024-02-01 08:49:47.221039');
INSERT INTO `django_migrations` VALUES (43, 'auth', '0008_alter_user_username_max_length', '2024-02-01 08:49:47.222041');
INSERT INTO `django_migrations` VALUES (44, 'auth', '0009_alter_user_last_name_max_length', '2024-02-01 08:49:47.224035');
INSERT INTO `django_migrations` VALUES (45, 'auth', '0010_alter_group_name_max_length', '2024-02-01 08:49:47.225032');
INSERT INTO `django_migrations` VALUES (46, 'auth', '0011_update_proxy_permissions', '2024-02-01 08:49:47.226029');
INSERT INTO `django_migrations` VALUES (47, 'auth', '0012_alter_user_first_name_max_length', '2024-02-01 08:49:47.228024');
INSERT INTO `django_migrations` VALUES (48, 'teacherhandler', '0001_initial', '2024-02-01 08:49:47.229021');
INSERT INTO `django_migrations` VALUES (49, 'studenthandler', '0001_initial', '2024-02-01 08:49:47.230024');
INSERT INTO `django_migrations` VALUES (50, 'classroomhandler', '0001_initial', '2024-02-01 08:49:47.232013');
INSERT INTO `django_migrations` VALUES (51, 'conversationhandler', '0001_initial', '2024-02-01 08:49:47.233011');
INSERT INTO `django_migrations` VALUES (52, 'sessions', '0001_initial', '2024-02-01 08:49:47.234008');
INSERT INTO `django_migrations` VALUES (53, 'classroomhandler', '0002_alter_robotclassroom_class_name', '2024-03-03 12:21:17.122350');
INSERT INTO `django_migrations` VALUES (54, 'teacherhandler', '0002_alter_teacheruser_have_classes', '2024-03-03 12:21:17.126340');
INSERT INTO `django_migrations` VALUES (55, 'teacherhandler', '0003_remove_teacheruser_have_classes', '2024-03-03 13:20:30.966307');
INSERT INTO `django_migrations` VALUES (56, 'classroomhandler', '0002_classroommessage', '2024-03-09 01:40:09.976945');
INSERT INTO `django_migrations` VALUES (57, 'classroomhandler', '0003_rename_message_type_classroommessage_user_type_and_more', '2024-03-09 01:45:37.696953');
INSERT INTO `django_migrations` VALUES (58, 'studenthandler', '0002_studentuser_student_avatar', '2024-03-14 01:16:54.175502');
INSERT INTO `django_migrations` VALUES (59, 'teacherhandler', '0004_teacheruser_teacher_avatar', '2024-03-14 01:16:54.237470');
INSERT INTO `django_migrations` VALUES (60, 'administratorhandler', '0002_meicymodel', '2024-03-21 03:03:59.149310');
INSERT INTO `django_migrations` VALUES (61, 'conversationhandler', '0002_conversation_rate', '2024-03-23 07:10:40.134234');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `session_data` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for studenthandler_studentuser
-- ----------------------------
DROP TABLE IF EXISTS `studenthandler_studentuser`;
CREATE TABLE `studenthandler_studentuser`  (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `phone_number` varchar(15) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(254) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `password` varchar(128) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `last_login_time` datetime(6) NOT NULL,
  `in_class` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `student_avatar` varchar(200) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`student_id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `phone_number`(`phone_number`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studenthandler_studentuser
-- ----------------------------
INSERT INTO `studenthandler_studentuser` VALUES (1, 'liguorui', '13013965912', '1606327882@2qq.com', 1, '1111', '2024-01-17 10:14:39.000000', '2', 'https://api.dicebear.com/7.x/miniavs/svg?seed=70');
INSERT INTO `studenthandler_studentuser` VALUES (2, 'zongmeixi', '18052126687', '251608312@qq.com', 1, '1111', '2023-12-12 10:15:27.000000', '20智72', 'https://api.dicebear.com/7.x/miniavs/svg?seed=1');
INSERT INTO `studenthandler_studentuser` VALUES (3, 'lihanwen', '13758472839', '1628382838@qq.com', 0, '123456', '2023-12-13 11:02:21.000000', '20智71', 'https://api.dicebear.com/7.x/miniavs/svg?seed=1');
INSERT INTO `studenthandler_studentuser` VALUES (4, 'yangwenkai', '1339291931', '162831231838@qq.com', 0, '123456', '2023-12-13 11:02:21.000000', '20智71', 'https://api.dicebear.com/7.x/miniavs/svg?seed=1');

-- ----------------------------
-- Table structure for teacherhandler_teacheruser
-- ----------------------------
DROP TABLE IF EXISTS `teacherhandler_teacheruser`;
CREATE TABLE `teacherhandler_teacheruser`  (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `phone_number` varchar(15) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(254) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `password` varchar(128) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `teacher_avatar` varchar(200) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`teacher_id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `phone_number`(`phone_number`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacherhandler_teacheruser
-- ----------------------------
INSERT INTO `teacherhandler_teacheruser` VALUES (1, 'lixiaobin', '1234431212', '21313@qq.com', 1, '1111', 'https://api.dicebear.com/7.x/miniavs/svg?seed=46');
INSERT INTO `teacherhandler_teacheruser` VALUES (2, 'kaihongmei', '19237162735', '14121211@qq.com', 1, '2222', 'https://api.dicebear.com/7.x/miniavs/svg?seed=1');
INSERT INTO `teacherhandler_teacheruser` VALUES (3, 'zhuyi', '13019293919', '21371727@qq.com', 1, '1111', 'https://api.dicebear.com/7.x/miniavs/svg?seed=1');

SET FOREIGN_KEY_CHECKS = 1;
