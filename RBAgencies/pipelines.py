# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class RbagenciesPipeline:
    def process_item(self, item, spider):
        adapt = ItemAdapter(item)
        if adapt.get('agency'):
            adapt['agency'] = adapt['agency'].replace('./Selection.aspx?agency=', '')
        return item
