import database.models as Models
import database.params as Parms
# import frameExtraction.sbdExtraction as SBDExtraction
import frameExtraction.mfExtraction as MFExtraction


def create_project(values):
    return Models.insert_one(Parms.TBNAME_PROJECTS, (Parms.PARAMS_PROJECTS['projecttitle'], Parms.PARAMS_PROJECTS['videotitle'], Parms.PARAMS_PROJECTS['videopath'],
                                                     ), values)


def get_projects():
    return Models.get_all(Parms.TBNAME_PROJECTS)


def get_project(id):
    return Models.get_one(Parms.TBNAME_PROJECTS, id)


def delete_project(id):
    return Models.delete_one(Parms.TBNAME_PROJECTS, id)


# def fe_shot_boundry_det(videoPath, videoFileName, method, treshold):
#     return SBDExtraction.shot_bundry_detection(videoPath, videoFileName, method, treshold)


def fe_manual_frame(videoPath, videoFileName, time):
    return MFExtraction.manual_frame(videoPath, videoFileName, time)