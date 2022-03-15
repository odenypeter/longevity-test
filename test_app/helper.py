import requests
import json

import pandas as pd


class MergeDataHelper:
    def __init__(self, request_data):
        self.request_data = request_data

    def merge_data(self):
        data_frames = []
        for item in self.request_data:
            data_frame = pd.DataFrame(
                self.get_data_from_app(item.get('data_url'))
            )

            data_frames.append(
                self.clean_data(
                    item.get('column_maps'),
                    data_frame
                )
            )
        # merge datasets
        if data_frames:
            merge_data = pd.concat(data_frames)
        else:
            merge_data = None

        if not merge_data.empty:
            return json.loads(merge_data.to_json(orient='records', lines=False))

    @staticmethod
    def get_data_from_app(url: str) -> pd.DataFrame:
        try:
            return requests.get(url).json()
        except json.JSONDecodeError:
            # perform error handling here
            return None

    def clean_data(self, column_maps, data_frame: pd.DataFrame):

        # rename the columns to match the app columns
        column_map = {item.get('incoming_column'): item.get('app_column') for item in column_maps}
        data_frame = data_frame.rename(columns=column_map)

        # select the app specific columns
        columns = [column.get('app_column') for column in column_maps]

        # select the columns:
        data_frame = data_frame[columns]

        # perform any data cleaning
        data_frame['field1'] = data_frame.apply(
            lambda x: self.clean_column_value(x.field1),
            axis=1
        )

        data_frame['field2'] = data_frame.apply(
            lambda x: self.clean_column_value(x.field2),
            axis=1
        )

        data_frame['field3'] = data_frame.apply(
            lambda x: self.clean_column_value(x.field3),
            axis=1
        )

        # return the clean data_frame
        return data_frame

    @staticmethod
    def clean_column_value(value):
        # perform all necessary cleaning on the values
        return f'{value}'
