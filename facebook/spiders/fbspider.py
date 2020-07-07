# -*- coding: utf-8 -*-
import scrapy

# response.xpath('/text()').extract()

class FbspiderSpider(scrapy.Spider):
    name = 'fbspider'
    allowed_domains = []
    # start_urls = input("Enter Profile URL...")
    # if len(start_urls)<1:
    start_urls = ['https://web.facebook.com/people/Faizan-Abbasi/100025535123020']
    # start_urls = ['https://web.facebook.com']

    def parse(self, response):


    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Extracting Work details
        company_name=[]
        company_details=[]
        work_describtion=[]
        
        work_list = response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]/ul/li').extract()
        
        for i in range(len(work_list)):
            company_name.append(response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]/ul/li['+str(i+1)+']/div/div/div/div/div[2]/div[1]/a/text()').extract())
            company_details.append(response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]/ul/li['+str(i+1)+']/div/div/div/div/div[2]/div[2]/div/text()').extract())
            work_describtion.append(response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]/ul/li['+str(i+1)+']/div/div/div/div/div[2]/div[3]/text()').extract())
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Extracting Professional Skills
        # skills=[]
        # skills_list = response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[2]/ul/li').extract()
        
        # for i in range(len(skills_list)):
        #     skills.append(response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[2]/ul/li['+str(i+1)+']/div/a/text()').extract())
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Extracting Education Details
        education_name=[]
        education_details=[]

        education_list = response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[3]/ul/li').extract()
        
        for i in range(len(education_list)):
            education_name.append(response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[3]/ul/li['+str(i+1)+']/div/div/div/div/div[2]/div[1]/a/text()').extract())
            education_details.append(response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[3]/ul/li['+str(i+1)+']/div/div/div/div/div[2]/div[2]/div/text()').extract())
            
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Extracting Current City and Home Town
        city_name=[]
        city_type=[]

        city_list = response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/ul/li').extract()

        for i in range(len(city_list)):
            city_name.append(response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/ul/li['+str(i+1)+']/div/div/div/div/div/div[2]/span/a/text()').extract())
            city_type.append(response.xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/ul/li['+str(i+1)+']/div/div/div/div/div/div[2]/div/text()').extract())

    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        yield{
            'Work': [company_name, company_details, work_describtion],
            'Education' : [education_name, education_details],
            'City/Home Town': [city_name, city_type]
        }