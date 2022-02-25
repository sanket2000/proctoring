import audio
import head_pose


if __name__ == "__main__":
    # main()
    t1 = th.Thread(target=head_pose.pose)
    t2 = th.Thread(target=audio.sound)
    # t3 = th.Thread(target=sound_analysis)

    t1.start()
    t2.start()
    # t3.start()

    t1.join()
    t2.join()
    # t3.join()
