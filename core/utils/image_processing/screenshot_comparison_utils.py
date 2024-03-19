#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, Any

import appium
from appium import webdriver


def compare_screenshots(driver: appium.webdriver, expected_screenshot: str, actual_screenshot: str) -> Dict[str, Any]:
    """
        :expected_screenshot, actual_screenshot - should be in base64 format

        Returns:
            The dictionary containing the following entries:

            visualization (bytes): base64-encoded content of PNG visualization of the current comparison
                operation. This entry is only present if `visualize` option is enabled
            count (int): The count of matched edges on both images.
                The more matching edges there are no both images the more similar they are.
            totalCount (int): The total count of matched edges on both images.
                It is equal to `count` if `goodMatchesFactor` does not limit the matches,
                otherwise it contains the total count of matches before `goodMatchesFactor` is
                applied.
            points1 (dict): The array of matching points on the first image. Each point is a dictionary
                with 'x' and 'y' keys
            rect1 (dict): The bounding rect for the `points1` array or a zero rect if not enough matching points
                were found. The rect is represented by a dictionary with 'x', 'y', 'width' and 'height' keys
            points2 (dict): The array of matching points on the second image. Each point is a dictionary
                with 'x' and 'y' keys
            rect2 (dict): The bounding rect for the `points2` array or a zero rect if not enough matching points
                were found. The rect is represented by a dictionary with 'x', 'y', 'width' and 'height' keys
    """

    options = {
        "visualize": True,
        "detectorName": "ORB",
        "matchFunc": "BruteForce",
        "goodMatchesFactor": 40
    }

    result = driver.match_images_features(expected_screenshot, actual_screenshot, **options)
    return result

def check_that_screenshot_contains_partial_image(driver: appium.webdriver, expected_partial_image: str, actual_screenshot: str) -> Dict[str, Any]:
    options = {
        "visualize": True
    }

    result = driver.find_image_occurrence(actual_screenshot, expected_partial_image, **options)
    return result

def get_screenshots_similarity(driver: appium.webdriver, expected_screenshot: str, actual_screenshot: str) -> Dict[str, Any]:
    options = {
        "visualize": True
    }

    result = driver.get_images_similarity(actual_screenshot, expected_screenshot, **options)
    return result

