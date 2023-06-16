import aiohttp
import asyncio

base_url = "https://purrbot.site/api"
urls = [
    "/list/nsfw/anal/gif",
    "/list/nsfw/blowjob/gif",
    "/list/nsfw/cum/gif",
    "/list/nsfw/fuck/gif",
    "/list/nsfw/neko/gif",
    "/list/nsfw/pussylick/gif",
    "/list/nsfw/solo/gif",
    "/list/nsfw/threesome_fff/gif",
    "/list/nsfw/threesome_ffm/gif",
    "/list/nsfw/yaoi/gif",
    "/list/nsfw/yaoi/gif"
]

webhook_url = ""

async def process_url(url):
    full_url = base_url + url
    print("Full URL:", full_url)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(full_url) as response:
                data = await response.json()
                links = data["links"]
                
                for link in links:
                    print("Link:", link)
                    
                    async with session.post(webhook_url, json={"content": link}) as webhook_response:
                        if webhook_response.status == 204:
                            print("Message sent to Discord webhook successfully.")
                        else:
                            print("Failed to send message to Discord webhook.")
        
    except aiohttp.ClientError as e:
        print("Error:", e)

async def main():
    await asyncio.gather(*[process_url(url) for url in urls])

if __name__ == "__main__":
    asyncio.run(main())
