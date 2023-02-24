from ytmusicapi import YTMusic
import re
import organize as o

file_path = "/Users/user/Desktop/PyYoutube/headers_auth.json"
ytmusic = YTMusic(file_path)


def k_to_number(viewsss):
    listtt = []
    for letters in viewsss:
        if letters == "K":
            if not re.search(r'.', viewsss):
                listtt.append('000')
            listtt.append('00')
        if letters == "M":
            if not re.search(r'.', viewsss):
                listtt.append('000000')
            listtt.append('00000')
        if letters == ".":
            listtt.append('')
        if letters not in ['K', ".", "M"]:
            listtt.append(letters)
    return int("".join(listtt))


class popular_videos:

    def __init__(self):
        pass

    def video_info(self, keyword, max_videos, filterr):
        search_results = ytmusic.search(
            query=keyword, limit=max_videos, filter='videos')
        i = 0
        list_of_names = []
        list_of_views = []
        list_of_links = []
        while i < max_videos:
            results = search_results[i]
            video_id = results['videoId']
            video_name = results['title']
            video_views = results['views']
            int_views = k_to_number(video_views)

            list_of_names.append(video_name)
            list_of_views.append(int_views)
            youtube_watch = 'https://www.youtube.com/watch?v='
            youtube_link = youtube_watch + video_id
            list_of_links.append(youtube_link)
            i += 1

        # Sort the video views in descending order
        sorted_views = o.ordered(list_of_views)
        sorted_names = []
        sorted_links = []
        for views in sorted_views:
            index = list_of_views.index(views)
            sorted_names.append(list_of_names[index])
            sorted_links.append(list_of_links[index])
            list_of_views[index] = None

        # Reverse the list to get the top videos first
        sorted_names.reverse()
        sorted_views.reverse()
        sorted_links.reverse()

        if filterr == "Views":
            return "\n".join(map(str, sorted_views))
        if filterr == "Title":
            return "\n".join(sorted_names)
        if filterr == "Links":
            return "\n".join(sorted_links)


resultss = popular_videos()


def search(keyword, maxx_video, typee):

    tuple_names = resultss.video_info(keyword, maxx_video, "Title")
    tuple_links = resultss.video_info(keyword, maxx_video, "Links")
    tuple_views = resultss.video_info(keyword, maxx_video, "Views")

    new_type = typee.lower()
    if re.search(r'link|url', new_type):
        print(
            f"Here are the top videos with the keyword '{keyword}'\n\n{tuple_links}")
    if re.search(r'title|name', new_type):
        print(
            f"Here are the top videos with the keyword '{keyword}'\n\n{tuple_names}")
    if re.search(r'view|stream|listen', new_type):
        print(
            f"Here are the top videos with the keyword '{keyword}'\n\n{tuple_views}")
