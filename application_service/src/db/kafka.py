from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from core import settings
from core import logger


class KafkaController:
    def __init__(self) -> None:
        self.admin = KafkaAdminClient(
            bootstrap_servers=[f"{settings.kafka_host}:{settings.kafka_port}"]
        )
        self.producer = KafkaProducer(
            bootstrap_servers=[f"{settings.kafka_host}:{settings.kafka_port}"]
        )

    async def kafka_create_topic(self, topic):
        try:
            topic_list = [NewTopic(name=topic, num_partitions=3, replication_factor=3)]
            self.admin.create_topics(new_topics=topic_list, validate_only=False)
        except:
            logger.info("Topic %s already existed", topic)

    async def kafka_send(self, topic, value, key):
        self.producer.send(
            topic=topic,
            value=value,
            key=key.encode("ascii"),
        )
        logger.info("New application was successfully load")


kafka_controller = KafkaController()
