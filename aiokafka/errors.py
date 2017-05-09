from kafka.errors import *  # noqa
from kafka.errors import KafkaError

__all__ = [
    # kafka-python errors
    "KafkaError", "ConnectionError", "NodeNotReadyError",
    "KafkaTimeoutError", "UnknownTopicOrPartitionError",
    "UnrecognizedBrokerVersion", "NotLeaderForPartitionError",
    "LeaderNotAvailableError", "TopicAuthorizationFailedError",
    "OffsetOutOfRangeError", "MessageSizeTooLargeError", "for_code", "NoError",
    "StaleMetadata", "CorrelationIdError", "NoBrokersAvailable",
    "RebalanceInProgressError", "IllegalGenerationError",
    "UnknownMemberIdError", "GroupLoadInProgressError",
    "GroupCoordinatorNotAvailableError", "NotCoordinatorForGroupError",
    "GroupAuthorizationFailedError",
    # aiokafka custom errors
    "ConsumerStoppedError", "NoOffsetForPartitionError", "RecordTooLargeError",
    "ProducerClosed"
]


class ConsumerStoppedError(Exception):
    """ Raised on `get*` methods of Consumer if it's cancelled, even pending
        ones.
    """


class NoOffsetForPartitionError(KafkaError):
    pass


class RecordTooLargeError(KafkaError):
    pass


class ProducerClosed(KafkaError):
    pass
