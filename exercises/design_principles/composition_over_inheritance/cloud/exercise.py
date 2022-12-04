from dataclasses import dataclass
from typing import Callable

from cloudengine import CloudProvider
from cloudengine.google import GoogleAuth

filter_func = Callable[[str, str, int], list[str]]


@dataclass
class ACCloud:
    bucket_name: str
    cloud_provider: CloudProvider

    def find_files(self, query: str, max_result: int) -> list[str]:
        response = self.cloud_provider.filter_by_query(
            bucket=self.bucket_name, query=query, max=max_result
        )
        return response["result"]["data"]


@dataclass
class PureACCloud:
    bucket_name: str
    filter_fn: filter_func

    def find_files(self, query: str, max_result: int) -> list[str]:
        return self.filter_fn(self.bucket_name, query, max_result)


def create_video_storage() -> ACCloud:
    cloud_provider = CloudProvider("eu-west-1c", GoogleAuth("something"), True)
    return ACCloud("video-backup.arjancodes.com", cloud_provider)


if __name__ == "__main__":
    cloud_provider = CloudProvider("de", GoogleAuth("something"), True)
    ac_cloud = ACCloud("bucket", cloud_provider)
    print(ac_cloud)
    print(ac_cloud.find_files("query", 5))

    video_storage = create_video_storage()
    print(video_storage)

    pure = PureACCloud("bucket", cloud_provider.filter_by_query)
