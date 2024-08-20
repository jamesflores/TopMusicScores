from django.contrib.syndication.views import Feed
from django.urls import reverse
from app.models import NewsItem


class LatestNewsFeed(Feed):
    title = "TopMusicScores.com"
    link = "/news/"
    description = "Updates on the latest sheet music products."

    def items(self):
        return NewsItem.objects.order_by('-published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:200] + '...' if len(item.content) > 200 else item.content

    def item_link(self, item):
        return reverse('news_item', args=[item.title_slug])
    
    def item_pubdate(self, item):
        return item.published