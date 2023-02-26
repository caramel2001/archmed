from archmed.slidesapi import create_TitleBody_slide, create_image_slide

# from summarization_and_qna_transformers import getAnswer, getSummary , clean_text
from archmed.summarization_and_qna_transformers import *
from archmed.pdf import preprocess

# INTRODUCTION SLIDE

# introductioncorp = "alkjf;lasjdf;laskjf;lakjf;laks"

# intro_txt = ""

# intro_txt += "The long-term success of the public health response to the coro- navirus disease 2019 (COVID-19) pandemic will depend on acquired immunity in a sufficient proportion of the population (herd immu- nity), which is estimated to be 67% for COVID-19 [1]. Achieving popu- lation immunity through natural means, or by allowing a large proportion of the population to become infected, would cause unprecedented strain on healthcare resources and could result in up to 30 million deaths worldwide [1]. Widespread vaccination is there- fore essential for managing COVID-19 transmission, although ques- tions remain about the degree and duration of protection that will be offered from COVID-19 vaccines [2]. However, the current pandemic is occurring amidst a backdrop of widespread mistrust in the safety and effectiveness of vaccines globally [3]. Thousands of people have taken to the streets around the world to protest COVID-19 social dis- tancing policies and the prospect of mass vaccinations. This is con- cerning as public attitudes towards vaccine safety, their importance, and effectiveness are consistently associated with vaccine uptake [3]. Although general population data from the UK and Europe indicate mostly positive attitudes towards vaccines, research is suggesting there is still a substantial (ffi 10%) proportion of adults who are"

# intro_txt += "unsure of or distrust the safety and effectiveness of vaccines in the UK and Europe general population [4]. Findings from nationally representative studies suggest unwill- ingness and uncertainty about receiving a COVID-19 vaccine will be a significant challenge in achieving the vaccination coverage required for population immunity. Early in the pandemic (April 2020), 26% of adults across seven European countries including the UK were unsure or unwilling to get a COVID-19 vaccine when available [5]. Other studies have found that around one-quarter of French [6] and US [7]. adults do not intend to receive the vaccine even if offered it. Research conducted later in the pandemic, in mid-July after restrictions had started to ease, revealed that an even greater proportion of the UK adult population (36%) was either unsure or definitely would not get the vaccine [8]. Women, [5,6,911] those with lower levels of educa- tion, [6,8,10] low income [6,7,10,11], who engage in fewer COVID-19 protective behaviours,[7] and who were not vaccinated against the flu in the past year are more likely to say they will refuse a COVID-19 vaccine when it becomes available [8,12]."

# intro_txt += "Concerns identified to date for intending not to receive the COVID-19 vaccine include worries about the newness and safety of the vaccine as well as about potential side effects [5,8,10,13]. The only study that has examined associations between general vaccine attitudes and intent to vaccinate against COVID-19 found confidence in vaccine safety to be the largest determinant [7]. However, to our knowledge no study has examined predictors of vaccine attitudes and how these attitudes in turn relate to an unwillingness to vacci- nate in the later context of the COVID-19 pandemic. Further missing from this work is information on determinants of uncertainty about receiving the COVID-19 vaccine, as prior research has only examined vaccine intent outcomes as binary (e.g. willing vs. unwilling) [5,6,9]. or as a continuous measure of vaccine likelihood [8]. Understanding factors driving uncertainty about being vaccinated against COVID-19 is crucial, as individuals who are uncertain may be the most realistic targets for public health communications programmes encouraging vaccination [14]. As these individuals make up a greater share of the population than those who are certain they would not vaccinate, understanding their concerns is paramount [5,8,9]. Consequently, there is an urgent need for a more updated and nuanced understanding of attitudes towards vaccines and factors determining vaccine intent in the context of the COVID-19 pandemic in order to tailor public health messaging accordingly [15]. Exploring predictors of vaccine attitudes in general terms whilst multiple vac- cine candidates are still being tested has the potential to help policy- makers identify and adapt interventions that increase vaccine confidence that have previously been tested outside the COVID-19 pandemic. It is crucial for public health that such work is undertaken before a vaccine is approved so that trust and willingness to be vacci- nated are high at the point that a COVID-19 vaccine is rolled out to maximise uptake among the general population. Therefore, the aims of the present study were to identify factors predictive of (1) a range of negative attitudes towards vaccines, and (2) uncertainty and lack of intent to vaccinate against COVID-19. Importantly, we utilise a large sample of UK adults who were asked about their vaccine atti- tudes and intentions at the beginning of a second wave of the COVID- 19 pandemic (September 2020) [16]."
# output_file = "/Users/pratham/Desktop/Ntution/data/output.pdf"
# intro_txt = clean_text(intro_txt)
# intro_summary = getSummary(intro_txt=intro_txt, dir="models")
# print(f"The summarised information is {intro_summary}")
# presentation_id = "1IQUpJg1t2LuCVKL4oN8YRZVj_LjfB9l9NcO5WkI0HfA"
# service, dservice = doOauthSlides()
# create_TitleBody_slide("INTRODUCTION", intro_summary, service, presentation_id)

# response = (
#     dservice.files()
#     .export(fileId=presentation_id, mimeType="application/pdf")
#     .execute()
# )
# with open(output_file, "wb") as f:
#     f.write(response)


def make_presentation(service, summary_texts: dict, presentation_id):
    for heading, content in summary_texts.items():
        if content["summary"] == "":
            continue
        if heading != "":
            if content["images"] is not None:
                create_image_slide(
                    heading,
                    content,
                    f"https://imagesarchmed.s3.ap-southeast-1.amazonaws.com/{content['images']}",
                    service,
                    presentation_id,
                )
            else:
                create_TitleBody_slide(
                    heading, content["summary"], service, presentation_id
                )


def make_Image_presentation(service, summary_texts: dict, presentation_id, url):
    for heading, content in summary_texts.items():
        if content == "":
            continue
        if heading != "":
            create_image_slide(heading, content, url, service, presentation_id)


def get_presentation_pdf(dservice, presentation_id, output_file):
    response = (
        dservice.files()
        .export(fileId=presentation_id, mimeType="application/pdf")
        .execute()
    )
    with open(output_file, "wb") as f:
        f.write(response)
