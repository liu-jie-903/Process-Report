import bpy

print("デバッグ: アーマチュアオブジェクト取得完了")
# アーマチュアオブジェクトを取得
vroid_armature = bpy.data.objects["Armature"]  # VRoidのアーマチュア名
bvh_armature = bpy.data.objects["1_wayne_0_1_8"]  # BVHのアーマチュア名


# ボーンの長さを計算する関数
def get_bone_length(armature, bone_name):
    bone = armature.pose.bones.get(bone_name)
    if bone is None:
        print(f"ボーン '{bone_name}' が見つかりません。")
        return None
    start = bone.head
    end = bone.tail
    return (end - start).length


# ボーンの長さを設定する関数
def set_bone_length(armature, bone_name, target_length):
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='EDIT')  # EDITモードに切り替え

    edit_bone = armature.data.edit_bones.get(bone_name)
    if edit_bone is None:
        print(f"ボーン '{bone_name}' が見つかりません。")
        bpy.ops.object.mode_set(mode='OBJECT')
        return

    direction = (edit_bone.tail - edit_bone.head).normalized()
    edit_bone.tail = edit_bone.head + direction * target_length

    bpy.ops.object.mode_set(mode='OBJECT')  # OBJECTモードに戻す


# VRoidの前腕の長さを取得
vroid_forearm_length = get_bone_length(vroid_armature, "J_Bip_L_LowerArm")

# BVHの前腕の長さを取得
bvh_forearm_length = get_bone_length(bvh_armature, "LeftForeArm")

# エラーチェックしてVRoidの前腕をBVHの長さに合わせる
if vroid_forearm_length is not None and bvh_forearm_length is not None:
    set_bone_length(vroid_armature, "J_Bip_L_LowerArm", bvh_forearm_length)

# 結果を出力
print("前腕の長さ:")
print(f"  VRoid: {vroid_forearm_length}")
print(f"  BVH  : {bvh_forearm_length}")
